from langchain_core.prompts import ChatPromptTemplate

initial_civilization_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a civilization simulation engine.

            Your task is to transform a user's civilization description
            into a plausible starting state for a long-term civilization simulation.

            Analyze the civilization's environment, economy, society,
            resources, military capability, infrastructure, and technological
            development described by the user.

            Generate realistic starting values based only on the information
            provided and reasonable historical or fictional assumptions.

            Do not make the civilization unrealistically powerful.
            The starting state should contain strengths and weaknesses.
            """
        ),
        (
            "human",
            """
            Civilization Description: {description}
            """
        ),
    ]
)

event_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the historical event engine for a civilization simulator.

Analyze the current state of the civilization and determine
whether a significant event should occur during this period.

Events should emerge naturally from the civilization's current
conditions.

Consider factors such as:

- population
- food availability
- wealth
- stability
- military strength
- technology
- infrastructure

Possible events include wars, political conflicts, economic
booms, famines, discoveries, technological breakthroughs,
natural disasters, migrations, social movements, and diplomatic
developments.

Do not force an event every period.

If no significant event is appropriate, return an event with
event_type set to "none" and significance set to 0.
"""
        ),
        (
            "human",
            """
Current civilization state: {state}
"""
        ),
    ]
)

consequence_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the consequence engine for a civilization simulator.

Analyze the historical event in the context of the civilization's
current state.

Determine realistic numerical changes caused by the event.

Consider both direct and indirect consequences.

Keep changes proportional to the significance of the event.
Do not make extreme changes unless the event is extremely severe.

Return zero for any attribute that should not meaningfully change.
"""
        ),
        (
            "human",
            """
Current civilization state:

{state}

Historical event:

{event}
"""
        ),
    ]
)