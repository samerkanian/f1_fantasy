import pytest
from f1_fantasy.scoring.computations import get_race_position_score, get_qualifying_position_score


@pytest.mark.parametrize(
    "position,expected",
    [
        (1, 100),
        (2, 90),
        (3, 85),
        (4, 78),
    ],
)
def test_race_scores(position, expected):
    """Test that race scores are correct"""
    points = get_race_position_score(position)
    assert points == expected


@pytest.mark.parametrize(
    "position,expected",
    [
        (1, 50),
        (2, 45),
        (3, 42.5),
        (4, 39),
    ],
)
def test_qualifying_scores(position, expected):
    """Test that race scores are correct"""
    points = get_qualifying_position_score(position)
    assert points == expected
