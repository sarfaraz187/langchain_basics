"""
Basic LangChain + OpenAI Example
This is a simple starter template demonstrating LangChain with OpenAI integration.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file based on .env.example and add your OpenAI API key.")
        return
    
    print("🚀 LangChain + OpenAI Starter Template")
    print("=" * 50)
    
    # Initialize ChatOpenAI model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    # Create messages
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hello! Can you explain what LangChain is in one sentence?")
    ]
    
    print("\n📤 Sending message to OpenAI...")
    
    # Get response
    response = llm.invoke(messages)
    
    print("\n📥 Response received:")
    print(f"\n{response.content}\n")
    print("=" * 50)
    print("✅ Example completed successfully!")


if __name__ == "__main__":
    main()
