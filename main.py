# main.py


from pprint import pprint

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

from langchain_core.messages import HumanMessage  # noqa: E402

# from src.agent_with_tools import agent  # noqa: E402
# response = agent.invoke(
#     {"messages": [HumanMessage(content="What is the square root of 16?")]}
# )
# pprint(response["messages"][-1].content)
# pprint(response)
from src.agent_with_web_search import agent  # noqa: E402

question = HumanMessage(content="Who is the chief minister of tamil nadu?")

response = agent.invoke({"messages": [question]})

pprint(response["messages"][-1].content)
