from typing import Any, Dict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()


@tool
def web_search(query: str) -> Dict[str, Any]:
    """Perform a web search using Tavily"""
    return tavily_client.search(query)


# web_search.invoke("Who is the current mayor of San Francisco?")

agent = create_agent(model="gpt-5-nano", tools=[web_search])
