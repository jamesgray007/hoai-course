# Python package dependencies:
# pip install openai
# pip install openai-agents

import asyncio
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, WebSearchTool, FileSearchTool

import os
from dotenv import load_dotenv
from agents.mcp.server import MCPServerSse

"""
This code shows how to use the agents-as-tools pattern. 
You may want a central agent to orchestrate a network of specialized agents, instead of handing off control. You can do this by modeling agents as tools.
"""

# Load environment variables from .env file
load_dotenv()

# Add your Zapier MCP Server URL to the .env file before running the code.
MCP_URL_SSE = os.getenv("ZAPIER_MCP_SERVER_URL_SSE")
if not MCP_URL_SSE:
    raise EnvironmentError(
        "Missing ZAPIER_MCP_SERVER_URL. Paste the server-specific Zapier MCP "
        "URL into your .env or export it in your shell."
    )

# ---- Configure to your Zapier MCP server (server-specific URL) -------
zapier_server = MCPServerSse(
    params={"url": MCP_URL_SSE},
    name="zapier-mcp",
    cache_tools_list=False, # The agent calls list_tools() every time it is run. This will cache the tools list.
)

# Define the agents
search_agent = Agent(
    name="Search Agent",
    instructions="You are a search agent that searches the web for relevant information.",
    tools=[WebSearchTool()],
    model="gpt-4o-mini",
    handoff_description="Web search agent for gathering the most relevant information from the web."
)
spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate messages to Spanish",
    model="gpt-4o-mini",
    tools = [],
    handoff_description="An english to spanish translator",
)
french_agent = Agent(
    name="french_agent",
    instructions="You translate messages to French",
    model="gpt-4o-mini",
    tools = [],
    handoff_description="An english to french translator",
)
writer_agent = Agent(
    name="writer_agent",
    instructions="You write a report on the most relevant information from the search, knowledge base, and translation agents.",
    model="gpt-4o-mini",
    tools = [],
    handoff_description="A writer agent for writing a report on the most relevant information from the search, knowledge base, and translation agents.",
)
publisher_agent = Agent(
    name="publisher_agent",
    instructions="You publish the report to the #random channel on Slack",
    model="gpt-4o-mini",
    tools = [],
    mcp_servers=[zapier_server],
    handoff_description="A publisher agent for publishing the report to one or more channels on Slack"
)
# This is the manager agent that orchestrates the other agents.
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You orchestrate the search, writer and translation agents. "
        "You use the search agent to find the most relevant information. "
        "You use the writer agent to write a report on the most relevant information from the search"
        "You use the spanish and french agents to translate messages."
        "You use the publisher agent to publish the report to one or more channels."
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
        publisher_agent.as_tool(
            tool_name="publish_report",
            tool_description="Publish the report to one or more channels.",
        ),
    ]
)

# This is the main function that runs the orchestrator agent.
async def main():

    # Run the orchestrator agent; trace is used to log the agent's actions and decisions.
    with trace("Orchestrator Agent"):
        orchestrator_result = await Runner.run(
            orchestrator_agent,
            input="Please find one news story or article about OpenAI published in the last 2 days then write a report of approximately 200 words on the most relevant information from the search including a title, summary, and source URL, translate the report to french and spanish."
        )

    # Add this to write to a file
    output_filename = "output/report.md"
    with open(output_filename, "w", encoding="utf-8") as md_file:
        md_file.write(orchestrator_result.final_output)
    print(f"Output also saved to {output_filename}")

    print(orchestrator_result)

    # Run the publisher agent to post the report to the #random channel on Slack
    async with zapier_server:
        # ---- Run a single turn ----------------------------------------------
        result = await Runner.run(publisher_agent, 
                                  input=orchestrator_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

