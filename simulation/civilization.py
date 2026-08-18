from graph.state import CivilizationState
from llm.chains import initial_civilization_chain

def create_civilization(description: str) -> CivilizationState:
    civilization = initial_civilization_chain.invoke(description)
    return {
        "civilization_name": civilization.civilization_name,
        "description": description,

        "year": 1,
        "population": civilization.population,
        "food": civilization.food,
        "wealth": civilization.wealth,

        "stability": civilization.stability,
        "military_strength": civilization.military_strength,

        "technology_level": civilization.technology_level,
        "infrastructure": civilization.infrastructure,

        "current_event": "",
        "event_history": [],

        "simulation_status": "running",
    }