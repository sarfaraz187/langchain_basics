"""
Example 3: Chains
Demonstrates how to create and use LangChain chains.
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
        temperature=0.7
    )
    
    print("Example 3: Chains")
    print("=" * 50)
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a creative writer."),
        ("human", "Write a short {genre} story about {topic} in {num_sentences} sentences.")
    ])
    
    # Create an output parser
    output_parser = StrOutputParser()
    
    # Create a chain using LCEL (LangChain Expression Language)
    chain = prompt | chat | output_parser
    
    print("\nGenerating a story...")
    print("-" * 50)
    
    # Invoke the chain
    result = chain.invoke({
        "genre": "science fiction",
        "topic": "artificial intelligence",
        "num_sentences": "3"
    })
    
    print(f"\n{result}\n")
    
    # Another example
    print("\nGenerating another story...")
    print("-" * 50)
    
    result = chain.invoke({
        "genre": "mystery",
        "topic": "a missing key",
        "num_sentences": "4"
    })
    
    print(f"\n{result}\n")
    
    # Multi-step chain example
    print("\nMulti-step chain example:")
    print("-" * 50)
    
    # First chain: Generate a topic
    topic_prompt = ChatPromptTemplate.from_messages([
        ("human", "Suggest a random interesting topic for a {subject} discussion.")
    ])
    topic_chain = topic_prompt | chat | output_parser
    
    # Second chain: Expand on the topic
    expand_prompt = ChatPromptTemplate.from_messages([
        ("human", "Write 2 sentences about: {topic}")
    ])
    expand_chain = expand_prompt | chat | output_parser
    
    # Execute the multi-step process
    topic = topic_chain.invoke({"subject": "technology"})
    print(f"\nGenerated topic: {topic}")
    
    expansion = expand_chain.invoke({"topic": topic})
    print(f"\nExpansion: {expansion}\n")


if __name__ == "__main__":
    main()
