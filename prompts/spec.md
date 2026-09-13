<!-- Same text as .claude/commands/spec.md, for tools other than Claude Code. Paste it into your AI tool. -->

Specification.

Write a specification from this conversation: my design notes and the list "Decisions from the interview". My notes are the main source; the interview decisions fill their gaps. Save it as `docs/specs/YYYY-MM-DD-<slug>.md` (today's date and a short slug for what is being built) unless I name another file; create the folder if it does not exist. Use exactly these five sections, in this order. Keep it short: a few lines per section, one or two pages in total.

1. Summary: what the code does and how, in two or three sentences.
2. Interface and constraints: function name, parameters, return type, behaviour for empty or trivial input. Then the constraints: allowed libraries and functions, any rules this project sets for the AI (for example an AGENTS.md), input size limits, whether inputs may be modified, and what the code does not do (for example no input validation, no sorting).
3. Algorithm: the state variables with their starting values, then numbered steps following my design (1, 2, 3; sub-steps as a, b, c under their step, never continuing the parent numbering). Put decisions my notes left implicit (tie handling, order of operations) as a "note" under the step they belong to.
4. Edge cases and test plan: my cases first, then any you add, marked "added", each with its expected output. This list is what goes into the tests; end with the command that runs them. Tests check outputs only. Do not put running time or complexity in the spec: I check that separately, after implementation.
5. Differences from my design and decisions I made: what the interview added; anything you changed, added, or left out on your own, with the reason; and, under the heading "Decisions I made", every point that my notes and the interview did not settle, with the choice you made and why. Do not leave open questions: decide, and list the decision here so I can overturn it. Write "none" if nothing.

Do not write code. After saving the file, stop and ask me to review it. I will edit it or say "spec confirmed".

Language: reply in the language I write in. If I write in Korean, write your answers and any Markdown file you create (the specification included, section titles too) in Korean. Code, identifiers, and comments stay in English.
