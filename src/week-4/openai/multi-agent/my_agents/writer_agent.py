# my_agents/writer_agent.py

import os
from dotenv import load_dotenv
from agents import Agent

# Load environment variables from .env, if any are needed for writer configuration
load_dotenv()

def create_writer_agent() -> Agent:
    """
    Factory function to create and configure the Writer Agent.
    """
    return Agent(
        name="Writer Agent",
        instructions=(
            "You write a report on the most relevant information from the search, knowledge base, "
            "and translation agents. Use concise language and structure the report clearly."
        ),
        handoff_description=(
            "A writer agent for composing a comprehensive report based on inputs from the web search, "
            "knowledge base, and translation agents."
        )
    )

__all__ = ["create_writer_agent"]
