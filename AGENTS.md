# Rules for this repository

This repository is coursework for Problem Solving and Algorithms (SKKU, Fall 2026). The student designs the algorithm. You implement it and review it. Follow these rules in every conversation.

1. Python standard library only. No third-party packages (no numpy, no pandas). Use plain lists, dicts, sets, and loops, so that the code can be traced by hand.
2. Do not write or modify any code until the student says "spec confirmed". Before that point, answer in prose only.
3. Whenever you make a decision the student did not state, list it under a heading "Decisions I made". Never fill a gap silently.
4. The student's test cases come first. Keep every test case the student wrote. You may add more, but mark them as yours.
5. Keep the implementation close to the steps in the confirmed specification (the newest file in `docs/specs/`). Do not replace the student's algorithm with a different one, even a faster one, unless the student asks.
6. Write code, identifiers, and comments in English. Keep functions short. No classes unless the spec asks for them.
7. Use the language the student writes in. If the student writes in Korean, answer in Korean and write every Markdown file you create (the specification included, section titles too) in Korean. If the student writes in English, use English.
8. Which Python built-ins and standard library functions the solution may use differs from repository to repository. The section "Allowed in this repository" below is the list for this one. Basic operations (indexing, arithmetic, comparisons, `len`, `range`, `append`, loops) are always fine. A function that carries out a whole step of the algorithm by itself (for example `max` with a `key`, `sorted`, `collections.Counter`) may be used only if that section allows it. A function that does not touch the algorithm, does one simple thing, and costs O(1) (for example `isinstance`, `abs`, `int`) may be used at your own judgement even if it is not listed, but you must report every such use under "Decisions I made". If you are not sure which kind a function is, ask before using it.

## Allowed in this repository

The point of this problem is to find the answer in one or two passes over the list, without sorting. So:

- Allowed in the solution: `set`, `dict`, `len`, `range`, `enumerate`, `min`, `max`, `abs`, `for` and `while` loops.
- Not allowed in the solution: `sorted`, `list.sort`, `heapq`, `bisect`, `itertools`, `collections`.
- The test file may use anything in the standard library.
