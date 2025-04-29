# agents/synthesizer_agent.py

from agents import Agent

def create_synthesizer_agent() -> Agent:
    """
    Factory function to create the Synthesizer Agent, which
    inspects outputs (e.g. translations), corrects them, and merges
    into a final response.
    """
    return Agent(
        name="Synthesizer Agent",
        instructions=(
            "You inspect translations or fragments from other agents, "
            "make any necessary corrections, then concatenate them into a "
            "final, polished response."
        ),
        handoff_description="Ensures quality and coherence of aggregated outputs."
    )

__all__ = ["create_synthesizer_agent"]