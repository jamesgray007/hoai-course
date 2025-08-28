import asyncio
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, WebSearchTool, FileSearchTool

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


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


# Load sports car agent instructions from markdown file
sports_car_instructions_path = os.path.join(os.path.dirname(__file__), "sports_car_agent_instructions.md")
sports_car_agent_instructions = load_instructions(sports_car_instructions_path)

sports_car_agent = Agent(
    name="Sports Car Agent",
    instructions=sports_car_agent_instructions,
    tools=[WebSearchTool()],
    model="gpt-4o-mini"
)

summarize_agent = Agent(
    name="Summarize Agent",
    instructions="You are a summarize agent that will summarize the sports car agent's output.",
    model="gpt-4o-mini"
)

# This is the manager agent that will orchestrate the sports car agent
manager_agent = Agent(
    name="Manager Agent",
    instructions="You are a manager agent that will orchestrate the sports car agent.",
    model="gpt-4o-mini",
    tools=[
        sports_car_agent.as_tool(
            tool_name="search_for_sports_cars",
            tool_description="Search for sports cars"
        ),
        summarize_agent.as_tool(
            tool_name="summarize_sports_cars",
            tool_description="Summarize the sports car agent's output"
        )
    ]
)

async def main():

    # Run the manager agent
    with trace("Manager Agent"):
        manager_result = await Runner.run(
            manager_agent,
            input="Please find me the best sports car for living in Austin, TX, and summarize the results."
        )

    print(manager_result)

if __name__ == "__main__":
    asyncio.run(main())


    


