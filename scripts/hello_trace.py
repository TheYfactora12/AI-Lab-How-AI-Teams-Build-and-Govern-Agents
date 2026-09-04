"""Log a synthetic setup trace; this is not a model call or evaluation."""
import os
import weave

PROJECT = "kevinmedeiros-masterclass/ai-lab-agent-governance"


@weave.op()
def normalize_name(name: str) -> str:
    return name.strip()


@weave.op()
def build_greeting(name: str) -> str:
    return f"Hello, {name}! Weave tracing is working."


@weave.op()
def hello_trace(name: str) -> dict:
    return {
        "message": build_greeting(normalize_name(name)),
        "data_source": "synthetic",
        "purpose": "setup_check",
        "uses_llm": False,
    }


def main():
    client = weave.init(PROJECT)
    result, call = hello_trace.call("AI Lab")
    client.flush()
    recorded = client.get_call(call.id)
    if recorded.exception or recorded.output != result or not result:
        raise RuntimeError("Trace readback did not match the setup result.")
    url = f"https://wandb.ai/{PROJECT}/weave/calls/{call.id}"
    print(f"PASS: Trace stored and read back: {url}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(f"## First Weave trace\n\n[Open verified trace]({url})\n\nSynthetic function trace with two nested operations. No model call or evaluation was performed.\n")
    weave.finish()


if __name__ == "__main__":
    main()
