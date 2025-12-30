from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "http",  # HTTP-based remote server
                "url": "http://localhost:8000/mcp",
            },
        }
    )

    tools = await client.get_tools()

    agent = create_agent("gpt-4o-mini", tools)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in NY?"}]}
    )

    print("Weather Agent Response:")
    print(weather_response["messages"][-1].content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
