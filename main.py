# main.py


from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

from src.agent_with_tools import square_root  # noqa: E402

# This is how you import modules in Python (like import/require in JS)
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage
# from pprint import pprint
# # Create an instance of the ChatOpenAI model
# # You'll need an OpenAI API key for this
# llm = ChatOpenAI(
#     model="gpt-4o-mini",  # or "gpt-4" if you have access
#     temperature=0.7,       # creativity level: 0 = deterministic, 1 = creative
#     max_retries=3,       # number of retries for failed requests
#     max_tokens=100
# )

# # Send a message and get a response
# response = llm.invoke([
#     HumanMessage(content="What is LangChain in one sentence?")
# ])

# # Print the response
# pprint(response.content)

# run_agent()
result = square_root(16)
print(f"The square root of 16 is: {result}")
