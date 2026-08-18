from simulation.civilization import create_civilization
from graph.workflow import build_simulation_graph


def main():

    description = input(
        "Describe your civilization:\n> "
    )

    simulation_end_year = int(
        input(
            "How many years should the civilization be simulated?\n> "
        )
    )

    initial_state = create_civilization(
        description,
        simulation_end_year
    )

    simulation_graph = build_simulation_graph()

    final_state = simulation_graph.invoke(
        initial_state
    )

    print("\n" + "=" * 50)
    print("CIVILIZATION SIMULATION COMPLETE")
    print("=" * 50)

    print(f"\nCivilization: {final_state['civilization_name']}")
    print(f"Final Year: {final_state['year']}")
    print(f"Population: {final_state['population']}")
    print(f"Food: {final_state['food']}")
    print(f"Wealth: {final_state['wealth']}")
    print(f"Stability: {final_state['stability']}")
    print(
        f"Military Strength: "
        f"{final_state['military_strength']}"
    )
    print(
        f"Technology Level: "
        f"{final_state['technology_level']}"
    )
    print(
        f"Infrastructure: "
        f"{final_state['infrastructure']}"
    )

    print(
        f"\nSimulation Status: "
        f"{final_state['simulation_status']}"
    )

    print("\nHistorical Events:")

    if final_state["event_history"]:
        for event in final_state["event_history"]:
            print(f"- {event}")
    else:
        print("No major events occurred.")


if __name__ == "__main__":
    main()