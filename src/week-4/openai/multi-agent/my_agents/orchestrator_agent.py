# my_agents/orchestrator_agent.py

from agents import Agent  
from my_agents.search_agent import create_search_agent
from my_agents.writer_agent import create_writer_agent
from my_agents.knowledge_base_agent import create_knowledge_base_agent
from my_agents.translation_agents import create_spanish_agent, create_french_agent

def create_orchestrator_agent() -> Agent:
    """
    Factory function to create the Orchestrator Agent that
    delegates work to the other specialized agents.
    """
    search_agent = create_search_agent()
    kb_agent = create_knowledge_base_agent()
    writer_agent = create_writer_agent()
    es_agent = create_spanish_agent()
    fr_agent = create_french_agent()

    return Agent(
        name="Orchestrator Agent",
        instructions=(
            "You orchestrate the search, knowledge base, and translation agents. "
            "Use `search_the_web` to gather articles, "
            "`write_report` to write a report on the most relevant information from the search, knowledge base, "
            "`search_knowledge_base` to fetch files, "
            "`translate_to_spanish` and `translate_to_french` for translations, "
            "then combine everything into a coherent answer."
        ),
        model="gpt-4o-mini",
        tools=[
            search_agent.as_tool(
                tool_name="search_the_web",
                tool_description="Search the web for the most relevant information."
            ),
            writer_agent.as_tool(
                tool_name="write_report",
                tool_description="Write a report on the most relevant information from the search, knowledge base."
            ),
            kb_agent.as_tool(
                tool_name="search_knowledge_base",
                tool_description="Search the knowledge base for relevant documents."
            ),
            es_agent.as_tool(
                tool_name="translate_to_spanish",
                tool_description="Translate text into Spanish."
            ),
            fr_agent.as_tool(
                tool_name="translate_to_french",
                tool_description="Translate text into French."
            ),
        ],
        handoff_description="Coordinates sub-agents to fulfill complex requests."
    )

__all__ = ["create_orchestrator_agent"]