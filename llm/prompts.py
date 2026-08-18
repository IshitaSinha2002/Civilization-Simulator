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