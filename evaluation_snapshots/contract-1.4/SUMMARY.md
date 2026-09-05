# Controlled evaluation results

Contract: bank-vendor-eval-v1.4

| Case | V1 final | V2 final | V2 gate rejected |
| --- | --- | --- | --- |
| C01 | pass | pass | 0 |
| C02 | pass | pass | 0 |
| C03 | block | block | 3 |
| C04 | pass | pass | 0 |
| C05 | block | review | 0 |

[v1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1)

v1 final verdict counts: {'pass': 3, 'block': 2}

[v2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a)

v2 final verdict counts: {'pass': 3, 'block': 1, 'review': 1}

All findings remain drafts for human review. A block is an assessment-quality decision, not a legal/vendor conclusion.