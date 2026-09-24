# 1. Summary

Return the smallest positive integer missing from an input list. Store positive values in a set, then check consecutive integers starting at 1. If the input violates the constraints, print the specified English message and terminate the program.

## 2. Interface and constraints

- Function: `smallest_missing_positive(values)`. Return an `int` for valid input; return 1 for an empty list.
- Input: a list of at most 100,000 integers. Reject `True` and `False`; allow zero, negative integers, and duplicates. Do not modify the input list.
- Invalid input: print `Please enter a list of at most 100,000 integers. Booleans are not allowed.` as one line to standard output, then raise `SystemExit(1)`. This terminates the whole program unless the caller intercepts the exception; there is no normal return value.
- Use only the Python standard library. The repository permits `set`, `dict`, `len`, `range`, `enumerate`, `min`, `max`, `abs`, loops, and basic operations. Use set `add` and membership checks to carry out the brief's steps.
- Use `isinstance` for validation, `print` for the error message, and `SystemExit` for termination. These implement the interview requirements without replacing the algorithm.
- Do not use `sorted`, `list.sort`, `heapq`, `bisect`, `itertools`, or `collections` in the solution. Do not convert strings to integers, automatically correct inputs, or add interactive input handling.
- Follow `AGENTS.md`: do not write or modify code until the student says `spec confirmed`. Keep the implementation close to this specification, use short functions and English identifiers and comments, and do not add classes. Tests may use anything in the standard library. Per the student's updated instruction, write documents in English and keep the conversation in Korean.

## 3. Algorithm

Initial state: `positive_values` is an empty set; `_candidate` is 1.

Before traversing the input, check that `values` is a list. Only then check that its length is at most 100,000. On failure, perform the invalid-input behavior in section 2.

1. Iterate through the input list.
   a. Check that the current element is an integer and is not a boolean. On failure, immediately perform the invalid-input behavior in section 2.
   b. Compare the current value with 0.
   c. If it is greater than 0, add it to `positive_values`.
   d. Stop after every element has been examined.
   - Note: validate elements and build the set in the same traversal. Duplicates occupy one set entry; the input list remains unchanged.
2. Check whether `_candidate` is in `positive_values`.
   a. If it is present, increase `_candidate` by 1.
   b. Check membership again for the new value.
   c. Stop when `_candidate` is absent.
3. Return `_candidate`.

## 4. Edge cases and test plan

Preserve all student-provided cases first.

| Source | Input | Expected result |
| --- | --- | --- |
| Student | `[]` | 1 |
| Student | `[1, 2, 3]` | 4 |
| Student | `[0, -1, -2]` | 1 |
| Student | `[1, 1, 2, 2]` | 3 |
| Student | `[2, 3, 4]` | 1 |
| Student | `[2, 4, 1, 6, 5, 3]` | 7 |
| Student | `[1, 2, 5, 6]` | 3 |
| Student's trace | `[3, 4, -1, 1]` | 2 |
| Added by assistant | A list containing 1 through 100,000 in order | 100001 |
| Added by assistant | A list containing 100,001 zeros | Invalid-input behavior |
| Added by assistant | Each of `None`, integer `1`, string `"123"`, and tuple `(1, 2)` | Invalid-input behavior |
| Added by assistant | Each of `[1, 2.0]`, `[1, "2"]`, and `[1, None]` | Invalid-input behavior |
| Added by assistant | Each of `[True]` and `[False]` | Invalid-input behavior |

For invalid input, expect the exact message in section 2 followed by a newline, printed once to standard output, and termination with exit code 1. Check return values for valid cases and output and termination results for invalid cases. Do not inspect internal variables or implementation details.

Keep `test_smallest_missing_positive.py` next to `smallest_missing_positive.py` in the repository root. Use one function per case and preserve student cases first. Retain the existing standard-library `unittest` runner, with a `__main__` block that runs all cases and reports each result. Run the tests with: `python test_smallest_missing_positive.py`.

## 5. Differences from my design and decisions I made

The interview added validation of the input container, length, and element types. Reject booleans; on invalid input, print the agreed English message and terminate the whole program. Preserve the original algorithm of collecting positive values in a set and searching from 1. Omit the brief's cost analysis as required by the specification-writing instructions; review it separately after implementation. This document is in English as requested by the student after the initial draft.

### Decisions I made

- Keep the existing function name and parameter, `smallest_missing_positive(values)`, to match the existing interface.
- Leave the input unchanged because the set-based design does not require modifying it.
- Use `isinstance` to check lists and integers, rejecting booleans separately. Accept list and integer subclasses. These calls perform type checks without carrying out the search algorithm.
- Use `print` to write the message once to standard output with a newline, and `SystemExit(1)` to terminate. This specifies the output destination and failure exit code.
- Check the container and length first, then validate elements while building the set to avoid a separate element-validation traversal.
- Expose the behavior through a function call without adding interactive input, matching the existing function interface.
- Add cases covering the length boundary and the interview's invalid-input requirements. Retain the existing standard-library `unittest` runner and all test cases when moving the test file to the repository root as requested by the student. Resolve subprocess working directories from the test file's parent directory; no import-path adjustment is needed when the files are adjacent.
