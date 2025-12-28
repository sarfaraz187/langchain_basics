# src/my_first_agent.py

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

from pprint import pprint  # noqa: E402

from langchain.agents import create_agent  # noqa: E402
from langchain_core.messages import AIMessage, HumanMessage  # noqa: E402
from pydantic import BaseModel  # noqa: E402


class DefinitionResponseStruc(BaseModel):
    name: str
    definition: str
    example: str

system_prompt = (
    "You are a helpful AI assistant that explains concepts in simple terms."
)

agent = create_agent(
    model="gpt-4o-mini",
    system_prompt=system_prompt,
    response_format=DefinitionResponseStruc,
)

def run_agent():
    # Use the agent to run a simple task
    response = agent.invoke({
        "messages": [
            HumanMessage(content="Explain LangChain in one sentence."),
            AIMessage(content=""),
            HumanMessage(content="Explain to me in simple terms in one sentence."),
        ]
    })
    pprint(response["messages"][-1].content)
    pprint(response)


# This ensures code only runs when file is executed directly
# using uv run src/my_first_agent.py, NOT when imported
if __name__ == "__main__":
    run_agent()
