from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

class InitialCivilization(BaseModel):
    civilization_name: str = Field(
        description="Name of the civilization"
    )

    description: str = Field(
        description="Short description of the civilization"
    )

    population: int = Field(
        description="Estimated starting population"
    )

    food: int = Field(
        description="Starting food availability from 0 to 100"
    )

    wealth: int = Field(
        description="Starting economic wealth from 0 to 100"
    )

    stability: int = Field(
        description="Political and social stability from 0 to 100"
    )

    military_strength: int = Field(
        description="Military strength from 0 to 100"
    )

    technology_level: int = Field(
        description="Starting technology level from 1 to 100"
    )

    infrastructure: int = Field(
        description="Infrastructure development from 0 to 100"
    )


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7
)

initial_civilization_chain = llm.with_structured_output(
    InitialCivilization
)