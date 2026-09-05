# V2 correction record: through contract 1.4

This record explains why V2 changed and keeps each experiment separate. Earlier outputs were preserved; expectations were not changed to manufacture a pass.

## Contract 1.2: structural and scope correction

The original offline review exposed malformed nested inputs and duplicate source identifiers. The first live comparison also exposed unsupported scope decisions and unreliable judge handling of unavailable output.

Shared validation, prompt, scorer and judge corrections applied to both versions. V2 alone added a post-generation gate that withholds unsupported behavioral-test claims and converts unresolved conditional scope to `needs_clarification`. Contract 1.2 demonstrated the C03 scope containment.

## Independent challenge after contract 1.2

A new test changed the finding type from `tested_in_scope` to `documented`. The V2 gate only inspected behavioral-test citations, so eight documentary-evidence mutations could remain review-ready:

- wrong vendor or use case;
- missing or unavailable source;
- invented quotation;
- wrong requirement binding;
- stale source;
- wrong system version.

The exact reference scorer caught five of the first variants after generation, but the application gate itself did not. Requirement, date and version mismatches for documentary citations were also outside the exact reference scorer. This was a real coverage gap.

## Contract 1.4: documentary boundary correction

V2 now validates every cited finding for source identity, use-case identity, system version, retrieval availability, requirement binding, review date window, passage identity and exact quote. Behavioral-test findings retain their additional method, result and limitation rules. If any check fails, V2 withholds the whole generated narrative, records the reasons and requires human review.

The dataset, answer key, prompt, model, scorers and judge remained unchanged. V1 remained unchanged. The only V1/V2 difference in contract 1.4 is the expanded post-generation gate.

## Current verification

- 23 assessment regression tests pass, including eight documentary-boundary subcases.
- Six intake tests pass.
- 31 offline adversarial probes meet their expectations with zero observed gaps.
- The [contract 1.4 workflow](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33972108376) completed both hosted evaluations.
- [V1](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1) produced three passes and two blocks with no application errors. Its C05 judge reasoning remains unreliable.
- [V2](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a) produced three passes, one block and one review. Its C05 generation failed schema validation and was safely withheld.

V2 C03 recorded three rejections: the two unknown-scope decisions and one citation bound to the wrong requirement. This is hosted evidence that the new rule ran, not only a unit-test result.

## Remaining limits

- One trial per case cannot estimate reliability or error rates.
- The model produced different C05 outcomes across otherwise controlled calls. Temperature zero is not a repeatability guarantee.
- C02's readiness mismatch still escapes the current graders.
- Whole-packet withholding can remove useful safe content.
- Exact citation checks do not prove a source is authentic or a claim is semantically true.
- The answer key has not received independent banking or GRC expert validation.
- Public-document assessment and calibrated numerical risk ratings remain outside this completed comparison.

The operating decision remains draft-only use with human review. See [the current comparison](CURRENT_COMPARISON.md) for the presentation evidence.
