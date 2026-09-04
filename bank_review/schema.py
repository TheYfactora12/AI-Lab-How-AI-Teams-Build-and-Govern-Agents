from typing import Literal
from pydantic import BaseModel, ConfigDict


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ScopeItem(StrictModel):
    requirement_id: str
    applicability: Literal["applicable", "not_applicable", "needs_clarification"]
    rationale: str


class Citation(StrictModel):
    evidence_id: str
    passage_id: str
    quote: str


class Finding(StrictModel):
    requirement_id: str
    claim: str
    evidence_status: Literal["asserted", "documented", "tested_in_scope", "missing", "retrieval_error", "conflicting"]
    citations: list[Citation]


class Question(StrictModel):
    requirement_id: str
    question: str
    owner: str


class Assessment(StrictModel):
    scope: list[ScopeItem]
    findings: list[Finding]
    questions: list[Question]
    packet_status: Literal["ready_for_human_review", "needs_evidence", "withheld"]
    human_review_required: bool
    pilot_approved: bool
