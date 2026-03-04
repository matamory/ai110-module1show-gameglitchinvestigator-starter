import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from logic_utils import check_guess

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
