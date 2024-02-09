from dataclasses import dataclass


@dataclass
class Driver:
    abbreviation: str
    name: str
    team_name: str
    grid_position: int
    finishing_position: int

    @classmethod
    def from_session_result(cls, session, abbreviation):
        driver_result = session.get_driver(abbreviation).to_dict()
        name = driver_result["FullName"]
        team_name = driver_result["TeamName"]
        dnf = driver_result.dnf
        grid_position = int(driver_result["GridPosition"])
        finishing_position = -1 if dnf else int(driver_result["Position"])
        return cls(abbreviation, name, team_name, grid_position, finishing_position)
