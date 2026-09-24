# Design Brief

Fill this in before you open the AI tool (pipeline steps 1 to 3). Do not edit it after the interview. Differences between this brief and the final spec belong in the spec (`docs/specs/`), section 5.

## 1. Problem, restated

Input: A list of up to 100,000 integers

Output: The smallest positive integer that does not appear in the list

Constraints and assumptions: The list may be empty; if it is, the result is 1. The list may contain zero, negative integers, and duplicate values. Only positive integers affect the result.

## 2. Edge cases with expected outputs (at least three)

One line per case: the input, the expected output, and why the case matters.

- Input: [] | Expected: 1 | Why: Tests the empty input case.
- Input: [1, 2, 3] | Expected: 4 | Why: Tests the case where all positive integers from 1 through the list length are present.
- Input: [0, -1, -2] | Expected: 1 | Why: Tests that zero and negative integers do not affect the result.
- Input: [1, 1, 2, 2] | Expected: 3 | Why: Tests that duplicate values do not affect the result.
- Input: [2, 3, 4] | Expected: 1 | Why: Tests the case where 1 is missing.
- Input: [2, 4, 1, 6, 5, 3] | Expected: 7 | Why: Tests that the input does not need to be sorted.
- Input: [1, 2, 5, 6] | Expected: 3 | Why: Tests that the smallest missing positive integer can be smaller than the maximum value in the input.

## 3. Algorithm

State (each variable and its starting value):

- positive_values: An empty set that will store positive integers from the input.
- _candidate: Starts at 1 and represents the current positive integer being checked.


Steps (numbered 1, 2, 3; sub-steps as a, b, c under their step; one concrete action per step; say what is compared with what, and when the loop stops):

1. Iterate through the input list.
   a. Compare each value with 0.
   b. If the value is greater than 0, add it to positive_values.
   c. Stop when every element in the input list has been examined.
2. Starting with _candidate = 1, check whether _candidate is in positive_values.
   a. If it is present, increase _candidate by 1.
   b. Compare the new value of _candidate with the values in positive_values again.
   c. Stop when _candidate is not present in positive_values.
3. Return _candidate as the smallest missing positive integer.


## 4. Trace on one small input

Input: [3, 4, -1, 1]

One line per step of your algorithm, with the values of the state variables after that step.

- start: positive_values = {}, _candidate = 1
- after step 1: positive_values = {1, 3, 4}, _candidate = 1
- after step 2: 1 is present, so _candidate = 2; 2 is not present, so the loop stops.
- after step 3: return 2

Result: 2

Matches the expected output? yes

## 5. Expected cost

Time complexity, with one sentence of reasoning: O(n), because the algorithm scans the input once and then checks consecutive positive integers in a set, where each membership check is expected O(1).

Extra space: O(n), because the set may contain up to all positive values from the input.

Is this fast enough for the size limit in the problem? Why?
- Yes. With at most 100,000 input values, an O(n) algorithm requires work proportional to the size of the input and should handle the limit efficiently.