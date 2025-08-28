"""
OpenAI Responses API - File Search

This script demonstrates how to use the OpenAI Responses API with file search 
functionality to query documents stored in a vector store.

Requirements:
- OpenAI API key
- Vector Store ID (from OpenAI platform)
- Python 3.10+
- Python virtual environment (.venv)
- Python libraries: openai, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install the required Python libraries into the virtual environment
3. Create a .env file in the root directory and add your OpenAI API key and Vector Store ID
4. Upload documents to OpenAI vector store via the platform
Note: this will already be in place if used the setup instructions in the local_setup.md file.

Author: James Gray
Last Updated: 2025-01-27
"""

# =====================================================================================
# DEPENDENCIES
# =====================================================================================
# Install these Python libraries into virtual environment (.venv) using Terminal:
#   pip install openai  # OpenAI Python library for interacting with OpenAI APIs
#   pip install python-dotenv  # Load environment variables from .env file
# Occasionally you will need to update these libraries to the latest version:
#   pip install --upgrade package_name_here
# python-dotenv reads key-value pairs from a .env file and loads them as 
# environment variables.

# =====================================================================================
# IMPORTS
# =====================================================================================
# Import Python libraries we will use
import json
import os
import textwrap
from dotenv import load_dotenv
from openai import OpenAI

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Your .env file should look like this:
# OPENAI_API_KEY=your_api_key
# VECTOR_STORE_ID=your_vector_store_id

# Load environment variables from the .env file
load_dotenv()

# Create local variables to store the API credentials
api_key = os.getenv("OPENAI_API_KEY")
vector_store_id = os.getenv("VECTOR_STORE_ID")

# Establish an OpenAI client using the API key
client = OpenAI(api_key=api_key)

# =====================================================================================
# FILE SEARCH WITH RESPONSES API
# =====================================================================================
# This code uses the OpenAI Responses API with file search tools to query
# documents stored in a vector store
# https://platform.openai.com/docs/api-reference/responses/create


def main():
    """Demonstrate file search functionality using OpenAI Responses API.
    
    This function sends a query to the OpenAI Responses API with file search
    capabilities enabled. The API will search through documents stored in the
    configured vector store to provide contextual answers based on the
    uploaded documents.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        ValueError: If required environment variables are not set.
        Exception: If there's an error with the OpenAI API call or response 
            processing.
        SystemExit: Called when an exception occurs to exit the program with 
            status 1.
    """
    
    # Validate required environment variables
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    if not vector_store_id:
        raise ValueError("VECTOR_STORE_ID environment variable is required")
    
    # Configure the user message - the question to search documents for
    prompt = "How do I reset my password?"
    
    try:
        # Generate a response using the OpenAI Responses API with file search
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            tools=[{
                "type": "file_search",
                "vector_store_ids": [vector_store_id]
            }],
            include=["file_search_call.results"]
        )
        
        # Display results
        print("Full Response Object (JSON):")
        print("-" * 50)
        # Convert response to JSON format for detailed inspection
        response_json = response.to_json()
        print(json.dumps(json.loads(response_json), indent=2))
        
        print("\nExtracted Answer:")
        print("-" * 50)
        print(response.output_text)
        
        print("\nFile Search Results:")
        print("-" * 50)
        # Display any file search results if available
        if hasattr(response, 'file_search_call') and response.file_search_call:
            print("Documents found and referenced in the response.")
        else:
            print("No specific file search results to display.")
            
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        print("Please check your .env file and ensure all required variables are set.")
        exit(1)
    except Exception as e:
        print(f"API Error: {e}")
        print("Please check your OpenAI API key and vector store configuration.")
        exit(1)


if __name__ == "__main__":
    main()