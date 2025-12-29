from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# web_search.invoke("Who is the current mayor of San Francisco?")

agent = create_agent(model="gpt-5-nano", tools=[], checkpointer=InMemorySaver())


def run_agent():
    question = HumanMessage(content="Hello my name is Mo. I like Formula 1 racing.")
    config = {"configurable": {"thread_id": "1"}}

    response = agent.invoke({"messages": [question]}, config)

    pprint(response["messages"][-1].content)

    question = HumanMessage(content="What is my name?")
    response = agent.invoke({"messages": [question]}, config)

    pprint(response["messages"][-1].content)


if __name__ == "__main__":
    run_agent()
