import asyncio
from openai import AsyncOpenAI
from agents import Agent
from agents.mcp import MCPServerStdio

async def main():
    # 1. Initialize the OpenAI client
    client = AsyncOpenAI()

    # 2. Launch a local filesystem MCP server via stdio
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

        # 3. List available tools on the filesystem server
        tools = await fs_server.list_tools()
        print("Filesystem tools:", [tool.name for tool in tools])

        # 4. Create an Agent that uses only this MCP server
        agent = Agent(
            name="FileAgent",
            instructions="Use the filesystem tools to search and read files.",
            mcp_servers=[fs_server],
            model="gpt-4o-mini",
            openai_client=client
        )

        # 5. Run the agent on a sample prompt
        response = await agent.run("List all the files in the samples directory")
        print("Agent response:", response.output)

    # Exiting the async with block will automatically clean up the subprocess

if __name__ == "__main__":
    asyncio.run(main())