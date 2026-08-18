from graph.state import CivilizationState
from llm.chains import (
    initial_civilization_chain,
    event_chain,
    consequence_chain
    )



def simulate_year(state: CivilizationState) -> CivilizationState:
    population = state["population"]
    food = state["food"]
    wealth = state["wealth"]

    # Population consumes food
    food_consumption = max(1, population // 1000)

    food -= food_consumption

    # Basic population change based on food availability
    if food > 60:
        population_growth = max(1, population // 100)
        population += population_growth

    elif food < 30:
        population_decline = max(1, population // 200)
        population -= population_decline

    # Economic change based on food availability
    if food > 50:
        wealth += 2
    elif food < 30:
        wealth -= 2

    return {
        **state,
        "year": state["year"] + 1,
        "population": max(0, population),
        "food": max(0, food),
        "wealth": max(0, wealth),
    }

def generate_event(state: CivilizationState) -> CivilizationState:
    event = event_chain.invoke(
        {
            "state": state
        }
    )

    if event.event_type == "none":
        return {
            **state,
            "current_event": "",
        }

    return {
        **state,
        "current_event": event.description,
        "event_history": state["event_history"] + [
            event.description
        ],
    }

def apply_event_consequences(
    state: CivilizationState
) -> CivilizationState:

    if not state["current_event"]:
        return state

    consequences = consequence_chain.invoke(
        {
            "state": state,
            "event": state["current_event"],
        }
    )

    return {
        **state,

        "population": max(
            0,
            state["population"] + consequences.population_change
        ),

        "food": max(
            0,
            state["food"] + consequences.food_change
        ),

        "wealth": max(
            0,
            state["wealth"] + consequences.wealth_change
        ),

        "stability": max(
            0,
            min(
                100,
                state["stability"] + consequences.stability_change
            )
        ),

        "military_strength": max(
            0,
            min(
                100,
                state["military_strength"]
                + consequences.military_strength_change
            )
        ),

        "technology_level": max(
            1,
            min(
                100,
                state["technology_level"]
                + consequences.technology_change
            )
        ),

        "infrastructure": max(
            0,
            min(
                100,
                state["infrastructure"]
                + consequences.infrastructure_change
            )
        ),
    }