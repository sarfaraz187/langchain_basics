"""
Example 1: Simple Chat Completion
Demonstrates basic chat completion with OpenAI using LangChain.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize the chat model
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    print("Example 1: Simple Chat Completion")
    print("=" * 50)
    
    # Single message
    messages = [
        HumanMessage(content="What are the top 3 benefits of using LangChain?")
    ]
    
    response = chat.invoke(messages)
    print(f"\nResponse:\n{response.content}\n")
    
    # Conversation with context
    print("\nConversation with context:")
    print("-" * 50)
    
    conversation = [
        SystemMessage(content="You are a Python programming expert."),
        HumanMessage(content="What is a list comprehension?"),
    ]
    
    response = chat.invoke(conversation)
    print(f"\nAssistant: {response.content}\n")
    
    # Continue the conversation
    conversation.extend([
        AIMessage(content=response.content),
        HumanMessage(content="Can you give me a simple example?")
    ])
    
    response = chat.invoke(conversation)
    print(f"Assistant: {response.content}\n")


if __name__ == "__main__":
    main()
