"""
OpenAI Responses API - Basic Request/Response

This script demonstrates how to use the OpenAI Responses API to generate a response to a prompt. 

Requirements:
- OpenAI API key
- Python 3.10+
- Python virtual environment (.venv)
- Python libraries: openai, rich, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install the required Python libraries into the virtual environment
3. Create a .env file in the root directory and add your OpenAI API key
Note: this will already be in place if used the setup instructions in the local_setup.md file.

Author: James Gray
Last Updated: 2025-07-21
"""

# =====================================================================================
# DEPENDENCIES
# =====================================================================================
# Install these Python libraries into virtual environment (.venv) using Terminal.
#   pip install openai  # OpenAI Python library for interacting with OpenAI APIs
#   pip install python-dotenv
#   pip install python-dotenv
# Occasionally you will need to update these libraries to the latest version:
#   pip install --upgrade package_name_here
# python-dotenv reads key-value pairs from a .env file and loads them as 
# environment variables.

# =====================================================================================
# IMPORTS
# =====================================================================================
# Import Python libraries we will use
import textwrap
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Your .env file should look like this:
# OPENAI_API_KEY=your_api_key

# this loads the environment variables from the .env file
load_dotenv() 
# Create a local variable and to store the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY") 

# establish an OpenAI client using the API key
client = OpenAI(api_key=api_key) 

# =====================================================================================
# PROMPT TO RESPONSES API
# =====================================================================================
# This code using the OpenAI Responses API to generate a response to the prompt
# https://platform.openai.com/docs/api-reference/responses/create

def main():
    """Demonstrate basic usage of OpenAI Responses API.
    
    This function sends a simple prompt to the OpenAI Responses API asking
    for the capital of Texas, with instructions to include a historical fact.
    It then displays both the full response object and the extracted answer.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        Exception: If there's an error with the OpenAI API call or response 
            processing.
        SystemExit: Called when an exception occurs to exit the program with 
            status 1.
    """
    
    # Configure the user message - the question or request to the LLM
    prompt = "What is the capital of New York?"
    
    # Configure the instructions for the AI assistant
    INSTRUCTIONS = (
        "Please provide a concise answer and include one interesting "
        "historical fact about the capital."
    )

    try:
        # generate a response to the prompt using the OpenAI Responses API
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            instructions=INSTRUCTIONS,
            tools=[] # No tools are needed for this simple prompt
        )

        # Display results
        print("Full Response Object:")
        print("-" * 50)
        print(json.dumps(response.model_dump(), indent=2))
        print("\nExtracted Answer:")
        print("-" * 50)
        print(response.output_text)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()