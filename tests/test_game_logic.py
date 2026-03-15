from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Challenge 1: Edge Case Tests
def test_decimal_input():
    # Decimal like 5.7 should be rejected as out of range or parsed to int
    ok, value, err = parse_guess("5.7")
    # Should either be ok with value=5, or rejected
    if ok:
        assert value == 5
    else:
        assert err is not None

def test_negative_input():
    # Negative numbers should be rejected
    ok, value, err = parse_guess("-1")
    assert ok == False
    assert err == "Guess must be between 1 and 100."

def test_out_of_range_high():
    # Numbers over 100 should be rejected
    ok, value, err = parse_guess("101")
    assert ok == False
    assert err == "Guess must be between 1 and 100."

def test_out_of_range_zero():
    # Zero should be rejected
    ok, value, err = parse_guess("0")
    assert ok == False
    assert err == "Guess must be between 1 and 100."

def test_non_numeric_input():
    # Text should be rejected
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert err == "That is not a number."

def test_empty_input():
    # Empty string should be rejected
    ok, value, err = parse_guess("")
    assert ok == False