from oa.common import short_error


def test_short_error_keeps_first_line_only():
    e = TimeoutError("GET timed out.\nCall log:\n  - cookie: oa_session=SECRET")
    assert short_error(e) == "TimeoutError: GET timed out."
    assert "SECRET" not in short_error(e)
    assert short_error(RuntimeError("x" * 500)) == "RuntimeError: " + "x" * 160
