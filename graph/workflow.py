from langgraph.graph import StateGraph, START, END

from graph.state import CivilizationState

from graph.nodes import (
    simulate_year,
    generate_event,
    apply_event_consequences,
    check_simulation,
)


def simulation_router(
    state: CivilizationState
) -> str:

    if state["simulation_status"] == "running":
        return "continue"

    return "end"


def build_simulation_graph():

    graph = StateGraph(CivilizationState)

    graph.add_node("simulate_year", simulate_year)
    graph.add_node("generate_event", generate_event)
    graph.add_node(
        "apply_event_consequences",
        apply_event_consequences
    )
    graph.add_node("check_simulation", check_simulation)

    graph.add_edge(
        START,
        "simulate_year"
    )

    graph.add_edge(
        "simulate_year",
        "generate_event"
    )

    graph.add_edge(
        "generate_event",
        "apply_event_consequences"
    )

    graph.add_edge(
        "apply_event_consequences",
        "check_simulation"
    )

    graph.add_conditional_edges(
        "check_simulation",
        simulation_router,
        {
            "continue": "simulate_year",
            "end": END,
        },
    )

    return graph.compile()