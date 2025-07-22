"""
OpenAI Responses API with MCP (Model Context Protocol) Integration

This script demonstrates how to use the OpenAI Responses API with a Zapier MCP 
server to create intelligent workflows. The example workflow searches the web for 
information about Google I/O 2025, summarizes the findings, emails the results, 
and posts to a Slack channel.

MCP (Model Context Protocol) allows agents to connect to external systems and 
tools through standardized server interfaces. This pattern works with any MCP 
server, not just Zapier.

Requirements:
- OpenAI API key
- Zapier MCP API key  
- Personal email configured
- Python 3.10+
- Python virtual environment (.venv)
- Python libraries: openai, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install the required Python libraries into the virtual environment
3. Create a .env file with required environment variables:
   - OPENAI_API_KEY=your_openai_api_key
   - ZAPIER_MCP_API_KEY=your_zapier_mcp_api_key
   - PERSONAL_EMAIL=your_email@example.com

References:
- OpenAI Responses API: https://platform.openai.com/docs/api-reference/responses
- OpenAI MCP Guide: https://openai.github.io/openai-agents-python/mcp/
- OpenAI Cookbook: https://cookbook.openai.com/examples/mcp/mcp_tool_guide

Author: James Gray
Last Updated: 2025-07-21
"""

# =====================================================================================
# DEPENDENCIES
# =====================================================================================
# Install these Python libraries into virtual environment (.venv) using Terminal:
#   pip install openai       # OpenAI Python library for Responses API
#   pip install python-dotenv # Environment variable management
# 
# Occasionally you will need to update these libraries to the latest version:
#   pip install --upgrade package_name_here

# =====================================================================================
# IMPORTS
# =====================================================================================
import json
import os
from typing import Dict, List, Optional

from dotenv import load_dotenv
from openai import OpenAI

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Load environment variables from .env file
load_dotenv()

# Required environment variables
REQUIRED_ENV_VARS = ["OPENAI_API_KEY", "ZAPIER_MCP_API_KEY", "PERSONAL_EMAIL"]

# Default configuration constants
DEFAULT_MODEL = "gpt-4o-mini"
ZAPIER_MCP_URL = "https://mcp.zapier.com/api/mcp/mcp"
SUMMARY_WORD_COUNT = "200-300"

def validate_environment() -> Dict[str, str]:
    """Validate that all required environment variables are present.
    
    Returns:
        Dict[str, str]: Dictionary containing validated environment variables.
        
    Raises:
        SystemExit: If any required environment variables are missing.
    """
    env_vars = {}
    missing_vars = []
    
    for var in REQUIRED_ENV_VARS:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        else:
            env_vars[var] = value
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {missing_vars}")
        print("Please ensure these are set in your .env file:")
        for var in missing_vars:
            print(f"  {var}=your_value_here")
        exit(1)
        
    return env_vars

def generate_workflow_prompt(personal_email: str) -> str:
    """Generate the workflow prompt for the AI assistant.
    
    Args:
        personal_email (str): The email address to send results to.
        
    Returns:
        str: The formatted prompt for the workflow.
    """
    return (
        f"Please search the web to research what Google announced at 2025 I/O "
        f"conference. Summarize what you found in {SUMMARY_WORD_COUNT} words, "
        f"email the summary to {personal_email}, and post the summary on the "
        f"Slack channel for my coworkers to see."
    )


def main():
    """Execute the MCP-enabled workflow using OpenAI Responses API.
    
    This function demonstrates a complete workflow that:
    1. Validates environment configuration
    2. Creates an OpenAI client with MCP tools
    3. Executes a multi-step workflow (web search, summarize, email, slack post)
    4. Displays the results
    
    The workflow uses Zapier MCP server to access external tools and services,
    enabling the AI to perform actions across multiple platforms automatically.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        SystemExit: If environment validation fails or API call encounters an error.
    """
    # Validate environment and get required variables
    env_vars = validate_environment()
    
    # Initialize OpenAI client
    client = OpenAI(api_key=env_vars["OPENAI_API_KEY"])
    
    # Generate workflow prompt
    prompt = generate_workflow_prompt(env_vars["PERSONAL_EMAIL"])
    
    # Developer message instructions
    INSTRUCTIONS = (
        "You are a helpful assistant that can search the web, summarize content, "
        "email results to a user, and post on a Slack channel. Execute all actions "
        "without asking for confirmation. Be thorough in your research and provide "
        "accurate, well-structured summaries."
    )
    
    try:
        print("Executing MCP-enabled workflow...")
        print(f"Workflow: {prompt}")
        print("-" * 80)
        
        # Execute the workflow using OpenAI Responses API with MCP tools
        response = client.responses.create(
            model=DEFAULT_MODEL,
            input=prompt,
            instructions=INSTRUCTIONS,
            tools=[
                {
                    "type": "mcp",
                    "server_label": "zapier",
                    "server_url": ZAPIER_MCP_URL,
                    "require_approval": "never",
                    "headers": {
                        "Authorization": f"Bearer {env_vars['ZAPIER_MCP_API_KEY']}"
                    },
                },
                {"type": "web_search_preview"}
            ]
        )
        
        # Display results
        print("Workflow completed successfully!")
        print("-" * 50)
        print("Response:")
        print(response.output_text)
        
        # Optional: Display full response object for debugging
        if os.getenv("DEBUG") == "true":
            print("\nFull Response Object (DEBUG):")
            print("-" * 50)
            print(json.dumps(response.model_dump(), indent=2))
            
    except Exception as e:
        print(f"Error executing workflow: {e}")
        print(
            "Please check your API keys, network connection, and that all "
            "required services (Zapier integrations) are properly configured."
        )
        exit(1)


if __name__ == "__main__":
    main()