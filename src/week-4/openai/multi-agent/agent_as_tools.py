# Python package dependencies:
# pip install openai
# pip install openai-agents

import asyncio
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, WebSearchTool, FileSearchTool

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

"""
This code shows how to use the agents-as-tools pattern. 
You may want a central agent to orchestrate a network of specialized agents, instead of handing off control. You can do this by modeling agents as tools.
"""

# Define the agents
search_agent = Agent(
    name="Search Agent",
    instructions="You are a search agent that searches the web for relevant information.",
    tools=[WebSearchTool(), FileSearchTool(vector_store_ids=[os.getenv("VECTOR_STORE_ID")])],
    model="gpt-4o-mini",
    handoff_description="Web search agent for gathering the most relevant information from the web."
)
spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate messages to Spanish",
    model="gpt-4o-mini",
    handoff_description="An english to spanish translator",
)
french_agent = Agent(
    name="french_agent",
    instructions="You translate messages to French",
    model="gpt-4o-mini",
    handoff_description="An english to french translator",
)
writer_agent = Agent(
    name="writer_agent",
    instructions="You write a report on the most relevant information from the search, knowledge base, and translation agents.",
    model="gpt-4o-mini",
    handoff_description="A writer agent for writing a report on the most relevant information from the search, knowledge base, and translation agents.",
)
# This is the manager agent that orchestrates the other agents.
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You orchestrate the search, writer and translation agents. "
        "You use the search agent to find the most relevant information. "
        "You use the writer agent to write a report on the most relevant information from the search"
        "You use the spanish and french agents to translate messages."
    ),
    model="gpt-4o-mini",
    tools=[
        search_agent.as_tool(
            tool_name="search_the_web",
            tool_description="Search the web for the most relevant information.",
        ),
        spanish_agent.as_tool(  
            tool_name="translate_to_spanish",
            tool_description="Translate messages to Spanish.",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate messages to French.",
        ),
        writer_agent.as_tool(
            tool_name="write_report",
            tool_description="Write a report on the most relevant information from the search,and translation agents.",
        ),
    ]
)

# This is the main function that runs the orchestrator agent.
async def main():

    # Run the orchestrator agent; trace is used to log the agent's actions and decisions.
    with trace("Orchestrator Agent"):
        orchestrator_result = await Runner.run(
            orchestrator_agent,
            input="Please search the web to find one news story or article about OpenAI published in the last 7 days then write a report of approximately 200 words on the most relevant information from the search, and then translate the report to french and spanish. Include the title, summary, and url in the report."
        )

    # Add this to write to a file
    output_filename = "output/report.md"
    with open(output_filename, "w", encoding="utf-8") as md_file:
        md_file.write(orchestrator_result.final_output)
    print(f"Output also saved to {output_filename}")

    print(orchestrator_result)

if __name__ == "__main__":
    asyncio.run(main())

