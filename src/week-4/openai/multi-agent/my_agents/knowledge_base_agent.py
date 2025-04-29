# agents/knowledge_base_agent.py

import os
from dotenv import load_dotenv
from agents import Agent, FileSearchTool

# Load environment variables (e.g., VECTOR_STORE_ID) from .env
load_dotenv()

def create_knowledge_base_agent() -> Agent:
    """
    Factory function to create and configure the Knowledge Base Agent.
    """
    return Agent(
        name="Knowledge Base Agent",
        instructions=(
            "You are a knowledge base agent that retrieves information from a vector-backed knowledge base. "
            "Use your tools to fetch relevant documents or passages."
        ),
        tools=[
            FileSearchTool(
                vector_store_ids=[
                    os.getenv(
                        "VECTOR_STORE_ID",
                        "vs_67d7245bd5a48191b1a81ccabca975e9"
                    )
                ]
            )
        ],
        handoff_description=(
            "Delegates knowledge-base queries and returns the top-matching files or summaries."
        )
    )

__all__ = ["create_knowledge_base_agent"]