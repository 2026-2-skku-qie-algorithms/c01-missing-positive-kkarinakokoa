<!-- Same text as .claude/commands/implement.md, for tools other than Claude Code. Paste it into your AI tool. -->

Implementation from the confirmed specification.

Read the specification: the file I name, or else the newest file in `docs/specs/`. Implement the interface it describes, following its algorithm steps in order. If a stub file for that interface already exists, fill it in; otherwise create one file named after the function.

Then write the tests: a plain test file next to the code, with one function per case in the spec's test plan (my cases first; no timing or complexity tests) and a `__main__` block that runs every test function and prints a line per test, so that it runs with `python <test file>` and needs no framework. If the project already uses a test framework, follow that instead. Run the tests.

Rules: use only the libraries and functions the spec allows, and follow any rules this project sets for the AI (for example an AGENTS.md); keep my algorithm; add nothing that is not in the spec.

When you are done, report:
- a short table mapping each spec step to the lines of code that carry it out
- the test results
- "Decisions I made": anything you had to decide that the spec did not say, including every simple O(1) helper you used that the allowed list does not name

Language: reply in the language I write in. If I write in Korean, write your answers and any Markdown file you create (the specification included, section titles too) in Korean. Code, identifiers, and comments stay in English.
