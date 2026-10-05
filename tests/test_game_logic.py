from logic_utils import check_guess, parse_guess

def test_winning_guess():
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_edge_case_string_and_empty_inputs():
    """Verify parse_guess gracefully handles empty, whitespace, or invalid text input."""
    ok, val, err = parse_guess("", 1, 100)
    assert not ok
    assert err == "Enter a guess."

    ok, val, err = parse_guess("abc", 1, 100)
    assert not ok
    assert err == "That is not a number."


def test_edge_case_out_of_bounds_numbers():
    """Verify parse_guess rejects numbers strictly outside the valid range."""
    ok, val, err = parse_guess("0", 1, 100)
    assert not ok
    assert "between 1 and 100" in err

    ok, val, err = parse_guess("150", 1, 100)
    assert not ok
    assert "between 1 and 100" in err


def test_edge_case_decimal_string_conversion():
    """Verify parse_guess converts float strings (e.g. '50.0') cleanly into integers."""
    ok, val, err = parse_guess("50.0", 1, 100)
    assert ok
    assert val == 50
    assert err is None