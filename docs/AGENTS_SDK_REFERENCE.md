# Optional OpenAI Agents SDK integration

Status: Reference supplied by the user; not installed, executed or adopted as the project architecture.

## What the supplied guide demonstrates

The pasted W&B guide describes instrumenting an OpenAI Agents SDK application with Weave. Its example defines a Wikipedia function tool, creates a research agent and runs three conversation turns with `Runner.run`, carrying forward the previous input list. According to that guide, the resulting agent, model and tool spans appear in Weave's Agents view.

The guide lists `weave`, `openai-agents` and `requests`, Python 3.10+, a W&B key and an OpenAI key as prerequisites for its example. These are example requirements, not a record of packages or credentials added to this project. Its “Install W&B MCP” text was part of the pasted source, not a separate installation request.

Official OpenAI background: [Agents documentation](https://developers.openai.com/api/docs/guides/agents). The exact W&B integration page URL was not included in the pasted material; the source hub is [Weave documentation](https://docs.wandb.ai/weave).

## Relationship to our existing V1

Our current application uses `weave.Model`, `@weave.op` and the OpenAI Python API client pointed at W&B Serverless Inference. It does not use the `openai-agents` framework, Agent or Runner. Its actual baseline is recorded in Calls/Traces and linked in [the saved review package](../REVIEW_START_HERE.md).

The API client package `openai` and the framework package `openai-agents` are different dependencies. Using the former does not mean our app already uses the latter. We have verified W&B inference with the existing W_B secret, not OpenAI-hosted inference credentials.

## Project decision

Keep the working baseline and the planned evidence-gate comparison intact. Treat an Agents SDK integration as a separate possible change, not an unrecorded addition to V2. If adopted, validate the integration and rerun the relevant baselines under the same evaluation contract. An Agents-view session is not itself proof that the assessment is correct or that a scored evaluation ran.

The Wikipedia research task is unrelated to our fixed synthetic banking evidence packets. It has not been run, and no live web-research tool has been added to the assessor.
