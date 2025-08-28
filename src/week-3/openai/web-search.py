"""
OpenAI Responses API - Web Search Integration

This script demonstrates how to use the OpenAI Responses API with web search 
capabilities to find and summarize current information from the internet.

Features:
- Web search integration using OpenAI's web_search_preview tool
- Automatic tool selection with tool_choice="auto"
- Response formatting with text wrapping

Requirements:
- OpenAI API key
- Python 3.10+
- Python virtual environment (.venv)  
- Python libraries: openai, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install required libraries: pip install openai python-dotenv
3. Create a .env file with your OpenAI API key
Note: Use setup instructions in local_setup.md if available.

Author: [Your Name]
Last Updated: [Date]
"""

# =====================================================================================
# DEPENDENCIES
# =====================================================================================
# Install these Python libraries into virtual environment (.venv):
#   pip install openai  # OpenAI Python library for API access
#   pip install python-dotenv  # Environment variable management

# =====================================================================================
# IMPORTS
# =====================================================================================
import textwrap
from openai import OpenAI
import os
from dotenv import load_dotenv

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Default instructions for web search responses
INSTRUCTIONS = (
    "Please provide a concise summary of the most significant AI news story "
    "from today. Include key details and sources when available."
)

# =====================================================================================
# WEB SEARCH FUNCTIONS
# =====================================================================================
# OpenAI Responses API with Web Search
# https://platform.openai.com/docs/api-reference/responses/create

def webSearch(query: str) -> str:
    """
    Search the web using OpenAI's Responses API and return summarized results.
    
    Args:
        query (str): The search query to find information about
        
    Returns:
        str: Summarized text response from the web search results
        
    Raises:
        Exception: If API call fails or returns invalid response
    """
    response = client.responses.create(
        model="gpt-4o",
        tools=[{"type": "web_search_preview"}],
        tool_choice="auto",  # Model decides which tool to use
        input=query,
        instructions=INSTRUCTIONS
    )
    return response.output_text

def main():
    """
    Main function to demonstrate web search functionality.
    
    Searches for AI news and displays formatted results.
    """
    try:
        query = "What was a top AI news story from OpenAI yesterday?"
        raw_response = webSearch(query)
        wrapped_response = textwrap.fill(raw_response, width=88)
        
        print("Web Search Results:")
        print("-" * 50)
        print(wrapped_response)
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()