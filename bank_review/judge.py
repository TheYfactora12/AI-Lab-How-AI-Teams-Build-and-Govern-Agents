import json
import os
from pathlib import Path
from typing import Literal
import weave
from openai import OpenAI
from bank_review.app import MODEL, PROJECT
from bank_review.schema import StrictModel


class Criterion(StrictModel):
    status: Literal["pass", "fail", "unknown"]
    reason: str
    evidence_refs: list[str]


class Judgment(StrictModel):
    evidence_support: Criterion
    scope_and_risk: Criterion
    follow_up_quality: Criterion
    verdict: Literal["pass", "review", "block"]
    rationale: str


def criterion_verdict(result):
    if any(result[k]["status"] == "fail" for k in ("evidence_support", "scope_and_risk")):
        return "block"
    if any(result[k]["status"] != "pass" for k in ("evidence_support", "scope_and_risk", "follow_up_quality")):
        return "review"
    return "pass"


def final_verdict(scores):
    exact = [scores.get(k, {}).get("status", "unknown") for k in ("score_references", "score_status")]
    judge = scores.get("BankRiskJudge", {}).get("verdict", "review")
    if "fail" in exact or judge == "block":
        return "block"
    if exact != ["pass", "pass"] or judge != "pass":
        return "review"
    return "pass"


class BankRiskJudge(weave.Scorer):
    model: str = MODEL
    rubric_id: str = "bank-risk-judge-v1.1"
    rubric: str
    catalog: dict

    @weave.op()
    def score(self, input: dict, expected: dict, output: dict | None) -> dict:
        if output is None:
            return {"verdict": "review", "error": "Application output unavailable", "rubric_id": self.rubric_id}
        # Do not expose app version or gate metadata to the judge.
        blinded = {k: v for k, v in output.items() if k != "gate_record"}
        client = OpenAI(base_url="https://api.inference.wandb.ai/v1", api_key=os.environ["WANDB_API_KEY"],
                        project=PROJECT, timeout=120, max_retries=0)
        try:
            response = client.chat.completions.create(
                model=self.model, temperature=0, max_tokens=3000, response_format={"type": "json_object"},
                messages=[{"role": "system", "content": self.rubric + "\nReturn JSON matching:\n" + json.dumps(Judgment.model_json_schema())},
                          {"role": "user", "content": json.dumps({"input": input, "expected": expected, "catalog": self.catalog, "assessment": blinded})}])
            if response.choices[0].finish_reason == "length":
                raise ValueError("Judge output truncated")
            result = Judgment.model_validate_json(response.choices[0].message.content).model_dump()
        except Exception as exc:
            return {"verdict": "review", "error": type(exc).__name__, "rubric_id": self.rubric_id}
        result["model_verdict"] = result["verdict"]
        result["verdict"] = criterion_verdict(result)
        result["rubric_id"] = self.rubric_id
        return result
