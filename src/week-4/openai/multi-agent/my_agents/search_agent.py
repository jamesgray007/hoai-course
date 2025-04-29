# my_agents/search_agent.py

import os
from dotenv import load_dotenv
from agents import Agent, WebSearchTool

# Load environment variables (e.g., API keys) from .env
load_dotenv()

def create_search_agent() -> Agent:
    """
    Factory function to create and configure the Search Agent.
    
    Returns:
        An Agent instance that can perform web searches.
    """
    return Agent(
        name="Search Agent",
        instructions=(
            "You are a search agent that performs web searches to find the most "
            "relevant information. Use your tools to query high-quality sources "
            "and return concise summaries."
        ),
        tools=[
            WebSearchTool(
                # You can customize tool parameters here if needed
                num_results=5,
                safe_search=True
            )
        ],
        handoff_description=(
            "Delegates web search queries and returns the top results with "
            "titles and URLs."
        )
    )

# Expose only the factory function in package imports
__all__ = ["create_search_agent"]