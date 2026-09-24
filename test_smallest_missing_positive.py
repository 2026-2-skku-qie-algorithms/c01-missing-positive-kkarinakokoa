"""Output tests for the confirmed specification."""

from pathlib import Path
import subprocess
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parent

from smallest_missing_positive import smallest_missing_positive


# Student-provided cases, including the design brief's trace.

def test_empty_list():
    assert smallest_missing_positive([]) == 1


def test_consecutive_values():
    assert smallest_missing_positive([1, 2, 3]) == 4


def test_nonpositive_values():
    assert smallest_missing_positive([0, -1, -2]) == 1


def test_duplicate_values():
    assert smallest_missing_positive([1, 1, 2, 2]) == 3


def test_missing_one():
    assert smallest_missing_positive([2, 3, 4]) == 1


def test_unsorted_values():
    assert smallest_missing_positive([2, 4, 1, 6, 5, 3]) == 7


def test_gap_below_maximum():
    assert smallest_missing_positive([1, 2, 5, 6]) == 3


def test_student_trace():
    assert smallest_missing_positive([3, 4, -1, 1]) == 2


# Added by assistant: input boundaries and validation cases.

def test_maximum_length():
    assert smallest_missing_positive(list(range(1, 100_001))) == 100001


def check_invalid_input(input_expression):
    script = (
        "from smallest_missing_positive import smallest_missing_positive\n"
        f"smallest_missing_positive({input_expression})\n"
        'print("Execution continued unexpectedly")\n'
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1, result
    assert result.stdout == (
        "Please enter a list of at most 100,000 integers. "
        "Booleans are not allowed.\n"
    ), result.stdout
    assert result.stderr == "", result.stderr


def test_excessive_length():
    check_invalid_input("[0] * 100_001")


def test_none_input():
    check_invalid_input("None")


def test_integer_input():
    check_invalid_input("1")


def test_string_input():
    check_invalid_input("\"123\"")


def test_tuple_input():
    check_invalid_input("(1, 2)")


def test_float_element():
    check_invalid_input("[1, 2.0]")


def test_string_element():
    check_invalid_input("[1, \"2\"]")


def test_none_element():
    check_invalid_input("[1, None]")


def test_true_element():
    check_invalid_input("[True]")


def test_false_element():
    check_invalid_input("[False]")


TEST_FUNCTIONS = (
    test_empty_list,
    test_consecutive_values,
    test_nonpositive_values,
    test_duplicate_values,
    test_missing_one,
    test_unsorted_values,
    test_gap_below_maximum,
    test_student_trace,
    test_maximum_length,
    test_excessive_length,
    test_none_input,
    test_integer_input,
    test_string_input,
    test_tuple_input,
    test_float_element,
    test_string_element,
    test_none_element,
    test_true_element,
    test_false_element,
)


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(
        unittest.FunctionTestCase(test) for test in TEST_FUNCTIONS
    )


if __name__ == "__main__":
    unittest.main(verbosity=2)
