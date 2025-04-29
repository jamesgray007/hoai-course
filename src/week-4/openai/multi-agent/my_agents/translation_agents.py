# agents/translation_agents.py

from agents import Agent

def create_spanish_agent() -> Agent:
    """
    Factory function to create an English→Spanish translation agent.
    """
    return Agent(
        name="Spanish Agent",
        instructions="You translate messages from English to Spanish, preserving meaning and tone.",
        handoff_description="An English-to-Spanish translator."
    )

def create_french_agent() -> Agent:
    """
    Factory function to create an English→French translation agent.
    """
    return Agent(
        name="French Agent",
        instructions="You translate messages from English to French, preserving meaning and tone.",
        handoff_description="An English-to-French translator."
    )

__all__ = ["create_spanish_agent", "create_french_agent"]