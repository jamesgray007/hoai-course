import asyncio
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from agents import (
    Agent, Runner,
    WebSearchTool, FileSearchTool, FunctionTool, function_tool
)

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

myagent = Agent (
    name = "My Agent",
    model = "gpt-4o-mini",
    instructions = (
        "You are an all-purpose assistant. Use your tools for web search, "
       " Answer concisely. Always pick the most "
        "relevant information from the web search results."
    ),
    tools = [
        WebSearchTool(),
    ]
)

async def main():
    """Main function to run the agent with a sample query."""
    goal = (
        "Find 3 AI news articles about Microsoft, OpenAI, and Google and summarize each one, then get "
        "the weather in Austin, TX today"
    )
    result = await Runner.run(myagent, input=goal)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())