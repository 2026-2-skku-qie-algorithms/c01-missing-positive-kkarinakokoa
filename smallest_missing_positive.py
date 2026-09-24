def smallest_missing_positive(values):
    """Return the smallest positive integer that does not appear in ``values``.

    See the spec in docs/specs/ for the exact behaviour.
    """
    positive_values = set()
    _candidate = 1
    error_message = (
        "Please enter a list of at most 100,000 integers. "
        "Booleans are not allowed."
    )

    if not isinstance(values, list) or len(values) > 100_000:
        print(error_message)
        raise SystemExit(1)

    for value in values:
        if not isinstance(value, int) or isinstance(value, bool):
            print(error_message)
            raise SystemExit(1)
        if value > 0:
            positive_values.add(value)

    while _candidate in positive_values:
        _candidate += 1

    return _candidate
