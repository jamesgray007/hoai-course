# This is a simple example of how to use the MCP tools to create an agent that can search the filesystem.
# https://openai.github.io/openai-agents-python/mcp/

import asyncio
import os
import shutil

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerStdio

async def main():
    
    #Launch a local filesystem MCP server via stdio
    my_dir = "/Users/jamesgray/Documents/Claude"
    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", 
                     my_dir],
        }
    ) as fs_server:
        # Under the hood, fs_server.connect() is called automatically,
        # but you can await it explicitly if you want to catch errors:
        await fs_server.connect()

        #List available tools on the filesystem server
        tools = await fs_server.list_tools()
        print("Filesystem tools:", [tool.name for tool in tools])

        # Create an Agent that uses only this MCP server
        agent = Agent(
            name="FileAgent",
            instructions="Use the filesystem tools to search and read files.",
            mcp_servers=[fs_server],
            model="gpt-4o-mini"
        )

        # Run the agent on a sample prompt
        response = await Runner.run(agent, "List all the files in the samples directory")
        print("Agent response:", response.final_output)

    # Exiting the async with block will automatically clean up the subprocess

if __name__ == "__main__":
    asyncio.run(main())