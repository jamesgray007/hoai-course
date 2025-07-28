"""Deterministic multi-agent workflow for AI news research and publishing.

This module implements a sequential workflow using OpenAI's Agent SDK to:
1. Research top AI stories from the web
2. Summarize and title the stories
3. Publish the results as markdown

The workflow is deterministic, meaning agents execute in a fixed sequence
with each agent's output feeding into the next agent's input.
"""

import asyncio
import os
from typing import Optional

from agents import Agent, Runner, trace, WebSearchTool, FileSearchTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration constants
DEFAULT_MODEL = "gpt-4o-mini"
RESEARCH_QUERY = "What are the top 5 AI stories in the last 7 days?"
SUMMARY_LENGTH_CHARS = "200-300"


def create_research_agent() -> Agent:
    """Create and configure the research agent.
    
    The research agent is responsible for scanning the web to find
    the top 5 AI stories from the last 7 days.
    
    Returns:
        Agent: Configured research agent with web search capabilities.
    """
    return Agent(
        name="Research Agent",
        instructions=(
            f"You are a research agent that scans the web for the top 5 AI stories "
            f"in the last 7 days. Provide comprehensive information about each story "
            f"including source, date, and key details."
        ),
        model=DEFAULT_MODEL,
        tools=[WebSearchTool()]
    )


def create_writer_agent() -> Agent:
    """Create and configure the writer agent.
    
    The writer agent takes research results and creates concise summaries
    with appropriate titles for each story.
    
    Returns:
        Agent: Configured writer agent for content summarization.
    """
    return Agent(
        name="Writer Agent",
        instructions=(
            f"You are a writer agent that summarizes stories into "
            f"{SUMMARY_LENGTH_CHARS} characters and creates compelling titles. "
            f"Focus on clarity, accuracy, and engagement. Ensure each summary "
            f"captures the key points and significance of the story."
        ),
        model=DEFAULT_MODEL,
        tools=[]
    )


def create_publisher_agent() -> Agent:
    """Create and configure the publisher agent.
    
    The publisher agent formats the final content as well-structured markdown
    suitable for publication.
    
    Returns:
        Agent: Configured publisher agent for content formatting.
    """
    return Agent(
        name="Publisher Agent",
        instructions=(
            "You are a publisher agent that formats content as clean, "
            "well-structured markdown. Use appropriate headers, formatting, "
            "and organization to create publication-ready content. "
            "Include proper markdown syntax for titles, links, and emphasis."
        ),
        model=DEFAULT_MODEL,
        tools=[]
    )


async def execute_research_phase(agent: Agent, query: str) -> str:
    """Execute the research phase of the workflow.
    
    Args:
        agent: The research agent to use.
        query: The research query to execute.
        
    Returns:
        str: Research results from the agent.
        
    Raises:
        RuntimeError: If the research phase fails.
    """
    try:
        result = await Runner.run(agent, input=query)
        return result.final_output
    except Exception as e:
        raise RuntimeError(f"Research phase failed: {e}") from e


async def execute_writing_phase(agent: Agent, research_data: str) -> str:
    """Execute the writing phase of the workflow.
    
    Args:
        agent: The writer agent to use.
        research_data: Research results to summarize.
        
    Returns:
        str: Summarized and titled content.
        
    Raises:
        RuntimeError: If the writing phase fails.
    """
    try:
        result = await Runner.run(agent, input=research_data)
        return result.final_output
    except Exception as e:
        raise RuntimeError(f"Writing phase failed: {e}") from e


async def execute_publishing_phase(agent: Agent, written_content: str) -> str:
    """Execute the publishing phase of the workflow.
    
    Args:
        agent: The publisher agent to use.
        written_content: Content to format for publication.
        
    Returns:
        str: Final formatted markdown content.
        
    Raises:
        RuntimeError: If the publishing phase fails.
    """
    try:
        result = await Runner.run(agent, input=written_content)
        return result.final_output
    except Exception as e:
        raise RuntimeError(f"Publishing phase failed: {e}") from e


async def chain_agents(research_query: Optional[str] = None) -> str:
    """Execute the complete deterministic agent workflow.
    
    This function orchestrates a three-phase workflow:
    1. Research: Find top AI stories using web search
    2. Writing: Summarize stories with titles
    3. Publishing: Format as markdown for publication
    
    Args:
        research_query: Optional custom research query. 
                       Defaults to RESEARCH_QUERY constant.
    
    Returns:
        str: Final published markdown content.
        
    Raises:
        RuntimeError: If any phase of the workflow fails.
    """
    query = research_query or RESEARCH_QUERY
    
    # Create agents
    research_agent = create_research_agent()
    writer_agent = create_writer_agent()
    publisher_agent = create_publisher_agent()
    
    try:
        # Configure tracing for the entire workflow chain
        with trace("chain_agents"):
            # Phase 1: Research
            research_result = await execute_research_phase(research_agent, query)
            
            # Phase 2: Writing
            writer_result = await execute_writing_phase(writer_agent, research_result)
            
            # Phase 3: Publishing  
            publisher_result = await execute_publishing_phase(
                publisher_agent, writer_result
            )
            
            print("\n" + "="*50)
            print("FINAL PUBLISHED CONTENT:")
            print("="*50)
            print(publisher_result)
            print("="*50)
            
            return publisher_result
            
    except Exception as e:
        raise RuntimeError(f"Agent workflow failed: {e}") from e


async def main() -> None:
    """Main entry point for the application.
    
    Raises:
        SystemExit: If the workflow fails critically.
    """
    try:
        await chain_agents()
    except RuntimeError as e:
        print(f"Application failed: {e}")
        raise SystemExit(1) from e
    except KeyboardInterrupt:
        print("Application interrupted by user")
        raise SystemExit(0)


if __name__ == "__main__":
    asyncio.run(main())