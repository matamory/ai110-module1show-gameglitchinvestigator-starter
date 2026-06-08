import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_hint_direction_regression_for_inversion_bug():
    high_outcome, high_message = check_guess(90, 50)
    low_outcome, low_message = check_guess(10, 50)

    assert high_outcome == "Too High"
    assert "LOWER" in high_message
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message


def test_check_guess_is_from_logic_utils_refactor():
    assert check_guess.__module__ == "logic_utils"


def test_get_range_for_difficulty_returns_expected_bounds():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_handles_numbers_and_invalid_input():
    assert parse_guess("60") == (True, 60, None)
    assert parse_guess("60.9") == (True, 60, None)
    assert parse_guess("abc") == (False, None, "That is not a number.")


def test_update_score_uses_attempt_number_for_win():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 5) == 60
