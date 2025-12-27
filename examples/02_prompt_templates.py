"""
Example 2: Prompt Templates
Demonstrates how to use prompt templates for reusable prompts.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.messages import HumanMessage

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize the chat model
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    print("Example 2: Prompt Templates")
    print("=" * 50)
    
    # Simple prompt template
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("human", "{text}")
    ])
    
    # Format the prompt
    messages = template.format_messages(
        input_language="English",
        output_language="Spanish",
        text="Hello, how are you?"
    )
    
    print("\nTranslation example:")
    response = chat.invoke(messages)
    print(f"Translation: {response.content}\n")
    
    # Another example with different parameters
    messages = template.format_messages(
        input_language="English",
        output_language="French",
        text="Good morning!"
    )
    
    response = chat.invoke(messages)
    print(f"Translation: {response.content}\n")
    
    # Code generation template
    code_template = ChatPromptTemplate.from_messages([
        ("system", "You are an expert programmer."),
        ("human", "Write a {language} function that {task}. Include comments.")
    ])
    
    print("\nCode generation example:")
    messages = code_template.format_messages(
        language="Python",
        task="calculates the factorial of a number"
    )
    
    response = chat.invoke(messages)
    print(f"\n{response.content}\n")


if __name__ == "__main__":
    main()
