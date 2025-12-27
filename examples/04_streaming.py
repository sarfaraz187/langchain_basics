"""
Example 4: Streaming Responses
Demonstrates how to stream responses from OpenAI for real-time output.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize the chat model
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        streaming=True
    )
    
    print("Example 4: Streaming Responses")
    print("=" * 50)
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "{question}")
    ])
    
    # Create a chain
    output_parser = StrOutputParser()
    chain = prompt | chat | output_parser
    
    print("\nStreaming response (token by token):")
    print("-" * 50)
    print("\nQuestion: What is the future of AI?\n")
    print("Response: ", end="", flush=True)
    
    # Stream the response
    for chunk in chain.stream({"question": "What is the future of AI? Answer in 3-4 sentences."}):
        print(chunk, end="", flush=True)
    
    print("\n")
    print("-" * 50)
    
    # Another streaming example
    print("\nAnother streaming example:")
    print("-" * 50)
    print("\nQuestion: Explain quantum computing in simple terms.\n")
    print("Response: ", end="", flush=True)
    
    for chunk in chain.stream({"question": "Explain quantum computing in simple terms in 2-3 sentences."}):
        print(chunk, end="", flush=True)
    
    print("\n")


if __name__ == "__main__":
    main()
