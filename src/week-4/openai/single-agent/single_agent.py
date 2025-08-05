import asyncio
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from agents import (
    Agent, Runner,
    WebSearchTool, FileSearchTool, FunctionTool, function_tool, ImageGenerationTool
)
from agents.tool import ImageGeneration

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def load_instructions(file_path: str) -> str:
    """Load agent instructions from a markdown file.
    
    Args:
        file_path (str): Path to the markdown file containing instructions.
        
    Returns:
        str: The contents of the instructions file.
        
    Raises:
        FileNotFoundError: If the instructions file doesn't exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Instructions file not found: {file_path}")
    except Exception as e:
        raise IOError(f"Error reading instructions file: {e}")


# Load instructions from markdown file
instructions_path = os.path.join(os.path.dirname(__file__), "agent_instructions.md")
agent_instructions = load_instructions(instructions_path)

myagent = Agent (
    name = "My Agent",
    model = "gpt-4.1-mini",
#    instructions = (
#        "You are an all-purpose assistant. Use your tools for web search, "
#        " Answer concisely. Always pick the most "
#        "relevant information from the web search results."
#    ),
    instructions = agent_instructions,  # Alternative: load from markdown file
    tools = [
        WebSearchTool(),
    ]
)

async def main():
    """Main function to run the agent with a sample query."""
    goal = (
        "Find 3 AI news articles about Microsoft, OpenAI, and Google and summarize each one, then get "
        "the weather in Austin, TX today."
    )
    result = await Runner.run(myagent, input=goal)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())