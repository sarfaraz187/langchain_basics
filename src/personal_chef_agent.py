# Personal chef Agent
# 1. Agent which takes in user's input which will be ingredients available
# 2. Agent suggests recipes based on available ingredients
# 3. Agent can remember user's dietary preferences using memory
from dotenv import load_dotenv

load_dotenv()

from pprint import pprint
from typing import Any, Dict

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from tavily import TavilyClient

tavily_client = TavilyClient()

model = "gpt-4o-mini"


@tool
def web_search(query: str) -> Dict[str, Any]:
    """Perform a web search using Tavily"""
    return tavily_client.search(query)


system_prompt = """You are a helpful recipe assistant that suggests recipes based on available ingredients.

Core Responsibilities:
- Suggest recipes using the ingredients provided by the user
- Remember and respect dietary preferences (vegetarian, vegan, allergies, etc.)
- Provide concise, actionable cooking instructions

Response Requirements:
- Keep responses short and to the point
- Always respond in JSON format
- Include cooking time and difficulty level when relevant

Response Structure (JSON):
{
    "recipe": "Recipe Name",
    "ingredients": [
        "ingredient1 with quantity",
        "ingredient2 with quantity"
    ],
    "instructions": "Clear step-by-step instructions numbered or separated by periods",
    "prep_time": "X minutes",
    "difficulty": "Easy/Medium/Hard"
}

Guidelines:
- If dietary restrictions are mentioned, store and apply them to all future suggestions
- If missing key ingredients, suggest simple substitutions
- Prioritize recipes that use most of the available ingredients
- Keep instructions practical and beginner-friendly
"""

personal_chef_agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt=system_prompt,
    checkpointer=InMemorySaver(),
)


def run_personal_chef_agent():
    question = HumanMessage(
        content="I have chicken, tomatoes, and rice. Suggest a recipe."
    )

    config = {"configurable": {"thread_id": "personal_chef_1"}}

    response = personal_chef_agent.invoke({"messages": [question]}, config)

    pprint(response["messages"][-1].content)

    pprint("---- Now asking for dietary preferences ----")
    question = HumanMessage(content="Remember that I am vegetarian.")
    response = personal_chef_agent.invoke({"messages": [question]}, config)
    pprint(response["messages"][-1].content)


if __name__ == "__main__":
    run_personal_chef_agent()
