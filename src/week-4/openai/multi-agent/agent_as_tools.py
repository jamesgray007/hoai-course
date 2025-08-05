"""
OpenAI Multi-Agent System - Agents as Tools Pattern

This script demonstrates the agents-as-tools pattern where a central orchestrator 
agent manages a network of specialized agents by calling them as tools rather than 
handing off control. This approach provides better coordination and control flow 
compared to traditional handoff patterns.

The system includes:
- Search Agent: Web search capabilities
- Translation Agents: Spanish and French translation
- Writer Agent: Report generation
- Publisher Agent: Slack publishing via Zapier MCP
- Orchestrator Agent: Central coordinator using other agents as tools

Requirements:
- OpenAI API key
- Zapier MCP Server URL
- Python 3.10+
- Python virtual environment (.venv)
- Python libraries: openai, openai-agents, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install required Python libraries: pip install openai openai-agents python-dotenv
3. Create a .env file and add your OpenAI API key and Zapier MCP Server URL
4. Configure Zapier integrations for Slack publishing

Author: James Gray
Last Updated: 2024-12-24
"""

# =====================================================================================
# DEPENDENCIES
# =====================================================================================
# Install these Python libraries into virtual environment (.venv) using Terminal:
#   pip install openai          # OpenAI Python library for AI model interactions
#   pip install openai-agents   # OpenAI Agents framework for multi-agent systems
#   pip install python-dotenv   # Environment variable management

# =====================================================================================
# IMPORTS
# =====================================================================================
# Standard library imports
import asyncio
import os

# Third-party imports
from dotenv import load_dotenv

# OpenAI Agents framework imports
from agents import (
    Agent, 
    ItemHelpers, 
    MessageOutputItem, 
    Runner, 
    trace, 
    WebSearchTool, 
    FileSearchTool
)
from agents.mcp.server import MCPServerSse

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Load environment variables from .env file
# Your .env file should contain:
# OPENAI_API_KEY=your_openai_api_key
# ZAPIER_MCP_SERVER_URL_SSE=your_zapier_mcp_server_url
load_dotenv()

# Validate required environment variables
MCP_URL_SSE = os.getenv("ZAPIER_MCP_SERVER_URL_SSE")
if not MCP_URL_SSE:
    raise EnvironmentError(
        "Missing ZAPIER_MCP_SERVER_URL_SSE. Paste the server-specific Zapier MCP "
        "URL into your .env file or export it in your shell."
    )

# =====================================================================================
# MCP SERVER CONFIGURATION
# =====================================================================================
# Configure Zapier MCP server for external integrations (Slack publishing)
zapier_server = MCPServerSse(
    params={"url": MCP_URL_SSE},
    name="zapier-mcp",
    cache_tools_list=False,  # Disables caching for dynamic tool discovery
)

# =====================================================================================
# AGENT DEFINITIONS
# =====================================================================================
# Define specialized agents that will be used as tools by the orchestrator

# Web search specialist agent
search_agent = Agent(
    name="Search Agent",
    instructions="You are a search agent that searches the web for recent information.",
    tools=[WebSearchTool()],
    model="gpt-4o-mini"
)

# Spanish translation specialist agent
spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate messages to Spanish",
    model="gpt-4o-mini",
    tools=[]
)

# French translation specialist agent
french_agent = Agent(
    name="french_agent",
    instructions="You translate messages to French",
    model="gpt-4o-mini",
    tools=[]
)

# Report writing specialist agent
writer_agent = Agent(
    name="writer_agent",
    instructions=(
        "You write a report on the most relevant information from the search, "
        "knowledge base, and translation agents."
    ),
    model="gpt-4o-mini",
    tools=[]
)

# Publishing specialist agent with Zapier MCP integration
publisher_agent = Agent(
    name="publisher_agent",
    instructions="You publish the report to the #random channel on Slack",
    model="gpt-4o-mini",
    tools=[],
    mcp_servers=[zapier_server]
)

# Central orchestrator agent that coordinates all other agents as tools
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You orchestrate the search, writer and translation agents. "
        "You use the search agent to find the most relevant information. "
        "You use the writer agent to write a report on the most relevant information from the search. "
        "You use the spanish and french agents to translate messages. "
        "You use the publisher agent to publish the report to one or more channels."
    ),
    model="gpt-4o-mini",
    tools=[
        search_agent.as_tool(
            tool_name="search_the_web",
            tool_description="Search the web for the most relevant information."
        ),
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate messages to Spanish."
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate messages to French."
        ),
        writer_agent.as_tool(
            tool_name="write_report",
            tool_description=(
                "Write a report on the most relevant information from the search "
                "and translation agents."
            )
        ),
        publisher_agent.as_tool(
            tool_name="publish_report",
            tool_description="Publish the report to one or more channels."
        ),
    ]
)


# =====================================================================================
# MAIN EXECUTION FUNCTION
# =====================================================================================
async def main():
    """Execute the multi-agent workflow using the agents-as-tools pattern.
    
    This function demonstrates a complete workflow where an orchestrator agent
    coordinates multiple specialized agents to:
    1. Search for recent OpenAI news articles
    2. Generate a comprehensive report
    3. Translate the report to French and Spanish
    4. Publish the results to Slack
    
    The orchestrator uses other agents as tools rather than handing off control,
    providing better coordination and oversight of the entire process.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        Exception: If there's an error during agent execution, file operations,
            or Zapier MCP server communication.
        EnvironmentError: If required environment variables are missing.
        FileNotFoundError: If the output directory doesn't exist.
    """
    
    # Define the task for the orchestrator agent
    task_prompt = (
        "Please find one news story or article about OpenAI published in the last 2 days "
        "then write a report of approximately 200 words on the most relevant information "
        "from the search including a title, summary, and source URL, translate the report "
        "to french and spanish."
    )
    
    try:
        # Execute the orchestrator agent with comprehensive tracing
        with trace("Orchestrator Agent"):
            orchestrator_result = await Runner.run(
                orchestrator_agent,
                input=task_prompt
            )

        # Save the orchestrator output to a markdown file
        output_filename = "output/report.md"
        with open(output_filename, "w", encoding="utf-8") as md_file:
            md_file.write(orchestrator_result.final_output)
        print(f"Orchestrator output saved to {output_filename}")

        # Display the orchestrator result
        print("\nOrchestrator Result:")
        print("-" * 50)
        print(orchestrator_result)

        # Publish the report to Slack using the publisher agent
        print("\nPublishing to Slack...")
        async with zapier_server:
            publish_result = await Runner.run(
                publisher_agent, 
                input=orchestrator_result.final_output
            )
            print("Report published successfully to Slack")
            
    except FileNotFoundError as e:
        print(f"File operation error: {e}")
        print("Ensure the 'output' directory exists")
        exit(1)
    except Exception as e:
        print(f"Error during agent execution: {e}")
        exit(1)


# =====================================================================================
# SCRIPT EXECUTION
# =====================================================================================
if __name__ == "__main__":
    asyncio.run(main())

