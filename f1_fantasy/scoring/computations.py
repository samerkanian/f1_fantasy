from f1_fantasy.scoring.constants import (
    POINTS_FOR_WIN,
    PODIUM_POSITION_DELTA,
    PODIUM_REFERENCE_POINTS,
    FINISHING_POSITION_DELTA,
    FINISHING_REFERENCE_POINTS,
)


def get_race_position_score(position):
    """A function to get the race points based on finishing position

    Parameters
    ----------
    position : int
        The finishing position of a a driver in qualifying

    Return
    ------
    float
        Race points for finishing position
    """

    # Special Cases: race win, podium
    if position == 1:
        return POINTS_FOR_WIN

    if position <= 3:
        return PODIUM_REFERENCE_POINTS - (position - 1) * PODIUM_POSITION_DELTA

    return FINISHING_REFERENCE_POINTS - (position - 1) * FINISHING_POSITION_DELTA


def get_qualifying_position_score(position):
    """Qualifying points are half that of the race position points

    Parameters
    ----------
    position : int
        The finishing position of a a driver in qualifying

    Return
    ------
    float
        Points for qualifying
    """

    # Qualifying points are half that of race results
    #   Decimals are allowed
    return get_race_position_score(position) / 2.0
