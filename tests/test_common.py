from oa.common import COLLEGE_ALIASES, COMPANY_ALIASES, canonical, short_error


def test_short_error_keeps_first_line_only():
    e = TimeoutError("GET timed out.\nCall log:\n  - cookie: oa_session=SECRET")
    assert short_error(e) == "TimeoutError: GET timed out."
    assert "SECRET" not in short_error(e)
    assert short_error(RuntimeError("x" * 500)) == "RuntimeError: " + "x" * 160



def test_canonical_names():
    assert canonical("IIT (ISM) Dhanbad", COLLEGE_ALIASES) == "IIT Dhanbad"
    assert canonical(" nit karnataka ", COLLEGE_ALIASES) == "NIT Surathkal"
    assert canonical("Zomato", COMPANY_ALIASES) == "Eternal (Zomato)"
    assert canonical("Eternal", COMPANY_ALIASES) == "Eternal (Zomato)"
    assert canonical("Qualcomm", COMPANY_ALIASES) == "Qualcomm"
