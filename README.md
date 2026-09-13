# C01 assignment: smallest missing positive

Problem Solving and Algorithms | Cycle 1 | Due Sun Sep 20, 2026, 23:59

Work in the order shown in class on Monday.

## The problem

> Given a list of integers, find the smallest positive integer that does not appear in the list. The list has at most 100,000 values.

Stub: `smallest_missing_positive.py` | Tests: `test_smallest_missing_positive.py`, created by the AI in step 6 from the test plan in the spec

Deciding what the statement leaves open is step 1.

## What to submit

Push to this repository before the deadline:

1. `DESIGN_BRIEF.md`, written before you opened the AI tool.
2. The spec in `docs/specs/`, confirmed by you, with section 5 (differences from the brief) filled in.
3. `smallest_missing_positive.py` and `test_smallest_missing_positive.py`, with every edge case from your brief as a test.

## Grading

This assignment is practice. Its purpose is to review the pipeline and get used to it. You get full credit for completing every step and pushing all three files. Gaps in your brief are not penalized; finding them during the interview and the spec is the point. What loses credit: a missing file, a spec you never confirmed, tests that do not run, or a brief written after you used the AI.

## How the pipeline runs in this repository

| Step | Who | Where |
|---|---|---|
| 1. Restate the problem | you, on paper | `DESIGN_BRIEF.md` section 1, 2 |
| 2. Write the algorithm as numbered steps | you, on paper | `DESIGN_BRIEF.md` section 3, 4, 5 |
| 3. Peer review | a classmate reads only your steps | in class (from Cycle 2) |
| 4. Requirements interview | AI reads the brief you hand it, then asks one question at a time about what is still open; you answer | `/interview I want to implement the algorithm in @DESIGN_BRIEF.md` |
| 5. Specification | AI drafts from the brief and your answers, you correct and confirm | `/spec` then edit the file it creates in `docs/specs/`, then say "spec confirmed" |
| 6. Implementation | AI | `/implement` (writes the code and the test file) |
| 7. Human review | you, before asking the AI | map code to steps, run the tests, check the cost |
| 8. Cross-review | AI, after your review | `/review` |

The slash commands are Claude Code commands defined in `.claude/commands/`. If you use another tool (Copilot, Codex, a chat interface), paste the same text from `prompts/`. The four prompts do not depend on this repository: they work from the notes you hand them and the conversation, so you can copy `prompts/` into any project of your own. `AGENTS.md` holds the rules the AI must follow in this repository, including which Python built-ins the solution may use for this problem (`CLAUDE.md` only points to it). Read it before step 1: your own steps have to fit the same list.

You may write to the AI, and write your own files, in Korean or in English. The AI answers and writes its files in the language you use; code stays in English.

Run the tests with:

```bash
python test_smallest_missing_positive.py
```
