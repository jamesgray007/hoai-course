# pip install openai openai-agents sseclient-py python-dotenv

# This code is an example of how to use the OpenAI Agents SDK with a Zapier MCP server.
# https://openai.github.io/openai-agents-python/mcp/
# This provides agents with access to any of the tools that are available in your Zapier MCP Server.


import os, asyncio
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp.server import MCPServerSse


# ---- Load the .env file ---------------------------------------------------
load_dotenv()

# Add your Zapier MCP Server URL to the .env file before running the code.
MCP_URL = os.getenv("ZAPIER_MCP_SERVER_URL")
if not MCP_URL:
    raise EnvironmentError(
        "Missing ZAPIER_MCP_SERVER_URL.  Paste the server-specific Zapier MCP "
        "URL into your .env or export it in your shell."
    )

# ---- Configure to your Zapier MCP server (server-specific URL) -------
zapier_server = MCPServerSse(
    params={"url": MCP_URL},
    name="zapier-mcp",
    cache_tools_list=True,
)

async def main(prompt: str):
    # Opens the SSE stream; when the block exits the SDK closes it cleanly
    async with zapier_server:
        # ---- Print discovered tools -----------------------------------------
        tools = await zapier_server.list_tools()
        print("\n🔧  Zapier tools discovered on this MCP server:")
        for tool in tools:                      # each item is a Tool object
            print(f" • {tool.name}")
        print("----------------------------------------------------------------\n")

        # ---- Build the agent -------------------------------------------------
        agent = Agent(
            name="Zapier Automation Assistant",
            instructions=(
                "You automate tasks via Zapier MCP. "
                "Confirm destructive requests before executing."
            ),
            model="gpt-4o-mini",
            mcp_servers=[zapier_server],
        )

        # ---- Run a single turn ----------------------------------------------
        result = await Runner.run(agent, input=prompt)   # returns RunResult
        print(result.final_output)                       # assistant’s reply

if __name__ == "__main__":
    asyncio.run(
        main("Add tomorrow 9 AM 'Monthly Ops Review' to my Google Calendar")
    )