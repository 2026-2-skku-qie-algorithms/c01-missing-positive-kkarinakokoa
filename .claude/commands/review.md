Cross-review. I have already reviewed the code myself. Now review it independently. Do not change any file.

Read the specification (the file I name, or else the newest file in `docs/specs/`), the implementation, and the tests. Report:

1. Spec conformance: any place where the code does something the spec does not say, or skips something the spec requires.
2. Counterexamples: try to construct an input on which the code gives a wrong answer. Show the input, the expected output, and what the code returns. If you cannot find one, say what you tried.
3. Edge cases: which cases from the spec are covered by tests, and which are not.
4. Complexity: the actual time and extra space of the code as written, including hidden costs such as `x in some_list` inside a loop, so that I can compare it with my own estimate.
5. Allowed functions: any library or function the code uses that the spec or the project's rules for the AI do not allow, and any small helper that was used without being reported.
6. Anything else a careful human reviewer would raise.

Be specific and short. I will compare your findings with mine and record what I missed.

Language: reply in the language I write in. If I write in Korean, write your answers and any Markdown file you create (the specification included, section titles too) in Korean. Code, identifiers, and comments stay in English.
