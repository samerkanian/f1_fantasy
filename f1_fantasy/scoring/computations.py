from f1_fantasy.scoring.constants import (
    POINTS_FOR_WIN,
    PODIUM_POSITION_DELTA_POINTS,
    PODIUM_REFERENCE_POINTS,
    FINISHING_POSITION_DELTA_POINTS,
    FINISHING_REFERENCE_POINTS,
    IMPROVEMENT_POINTS_PER_POSITION,
    RACE_COMPLETION_POINTS,
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

    # Special Cases: race win, podium, DNF
    if position == 1:
        return POINTS_FOR_WIN

    elif position <= 3:
        return PODIUM_REFERENCE_POINTS - (position - 1) * PODIUM_POSITION_DELTA_POINTS

    elif position == -1:
        return 0.0

    return FINISHING_REFERENCE_POINTS - (position - 1) * FINISHING_POSITION_DELTA_POINTS


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


def get_improvement_score(grid_position, finishing_position):
    if finishing_position == -1:
        return 0
    elif finishing_position < grid_position:
        return (grid_position - finishing_position) * IMPROVEMENT_POINTS_PER_POSITION
    else:
        return 0


def get_race_completion_score(num_driver_laps, num_laps):
    return (float(num_driver_laps) / num_laps) * RACE_COMPLETION_POINTS
