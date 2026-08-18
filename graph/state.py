from typing import TypedDict, List

class CivilizationState(TypedDict):
    civilization_name: str
    description: str

    year: int

    population: int
    food: int
    wealth: int

    stability: int
    military_strength: int

    technology_level: int
    infrastructure: int

    current_event: str
    event_history: List[str]

    simulation_status: str