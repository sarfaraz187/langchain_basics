from langchain.agents import create_agent
from langchain.tools import tool


@tool
def square_root(x: float) -> float:
    """Calculate the square root of a number"""
    return x**0.5


agent = create_agent(
    model="gpt-5-nano",
    tools=[square_root],
    system_prompt=(
        "You are an arithmetic wizard. "
        "Use your tools to calculate the square root and square of any number."
    ),
)
