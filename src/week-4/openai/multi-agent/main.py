import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from my_agents.orchestrator_agent import create_orchestrator_agent

load_dotenv()

async def main():
    orchestrator = create_orchestrator_agent()
    result = await orchestrator.run(
        input="Please find the top AI news today, then summarize the article, and translate the title, summary, and url to Spanish and French."
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())