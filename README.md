# One AI Assistant

This private repository holds one AI Assistant of one customer: a Claude skill, and the same content as a Claude plugin, built
for one business process from the customer's own documents. It runs in the customer's Claude, not on a server of ours.

The procedure that builds it is the skill `vibemaestro-gitops:assistant-procedure`; a coordinating session runs it, worker
sessions do the work, the owner approves, and the domain experts named in the spec sign off the key and each ruling.

| Folder | What it holds | Who writes it |
|---|---|---|
| `inputs/` | the customer's documents, as received | the intake (stage 2), never edited after |
| `assistant/` | the skill (`SKILL.md`, `scripts/`, `reference/`) and its plugin manifest `.claude-plugin/plugin.json` | the build (stage 3); frozen by the tag `v<n>` |
| `cases/dev/` | development cases | the build; a used test set moves here |
| `cases/test-v<n>/` | the test cases of version `n` and their expected results (the key) | a separate session, after the tag `v<n>` |
| `eval/` | `eval/v<n>.md`: the scores and the expert rulings | the scoring session (stage 5) |
| `dist/` | the skill zip, the plugin zip, the handover PDF | the packaging (stage 6) |
| `kb/` | the intent and the spec | stage 2 |

What is frozen when: the scoring thresholds at the spec's approval; `assistant/` at the tag `v<n>`; the test set and its key
when the domain experts sign it off. After that only expert rulings are added, each recorded in `eval/v<n>.md`.

No secret, token or password goes into this repository.
