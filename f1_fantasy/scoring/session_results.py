from f1_fantasy.scoring.computations import (
    get_race_position_score,
    get_improvement_score,
    get_race_completion_score,
    get_qualifying_position_score,
)


def calc_points_for_race(driver, session):
    """A function to tally points for a driver in a race session"""

    # Points based on finishing position
    race_position_points = get_race_position_score(driver.finishing_position)
    # Points based on number of improved positions
    improvement_points = get_improvement_score(driver.grid_position, driver.finishing_position)

    num_laps_completed = len(session.laps.pick_driver(driver.abbreviation))
    # Points based on completing part of the race
    completion_points = get_race_completion_score(num_laps_completed, session.total_laps)

    return race_position_points + improvement_points + completion_points


def calc_points_for_qualifying(driver):
    # Points based on finishing position
    return get_qualifying_position_score(driver.finishing_position)
