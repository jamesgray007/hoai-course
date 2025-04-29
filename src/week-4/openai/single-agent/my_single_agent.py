# single_agent_with_function_tools.py

# pip install openai
# pip install openai-agents
# pip install requests
# pip install python-dotenv

import asyncio
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from agents import (
    Agent, Runner,
    WebSearchTool, FileSearchTool,FunctionTool, function_tool
)

api_key = os.getenv("OPENAI_API_KEY")

@function_tool
def get_weather(latitude: float, longitude: float):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=30.380&longitude=-97.893&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&temperature_unit=fahrenheit")
    data = response.json()
    return data['current']['temperature_2m']

@function_tool
def summarize_text(text: str, max_length: int) -> str:
    """Produce a concise summary of the input text."""
    return text[:max_length] + "..."

@function_tool
async def get_ai_news():
  # Call Responses API with the web_search tool
    client = OpenAI(api_key=api_key)
    resp = client.responses.create(
        model="gpt-4o",
        input="Find the top AI news articles on the web for Anthropic, OpenAI, Google, and Meta over the last 7 days",
        tools=[{"type": "web_search"}]
    )

    # The API returns a list: first a web_search_call, then the assistant message
    for event in resp.output:
        if event.type == "message":
            # Return the assistant’s text content
            return event.content[0].text

    return "No web search results found."

def create_my_agent() -> Agent:
    """
    Create a versatile agent equipped with multiple built-in and custom tools.
    """
    return Agent(
        name="James Personal Agent",
        instructions=(
            "You are an all-purpose assistant. Use your tools for web search, "
            "finding my favorite AI news articles on the web, getting the weather, and summarization. "
            "Answer concisely."
            "Always pick the most relevant tool to use based on the user's request."
        ),
        tools=[
            WebSearchTool(),
            FileSearchTool(vector_store_ids=[os.getenv("VECTOR_STORE_ID")]),
            get_weather,
            get_ai_news,
            summarize_text
        ],
        handoff_description="Agent orchestrating multiple tools in a single loop."
    )

async def main():
    agent = create_my_agent()
    query = (
        "Find my favorite AI news articles and summarize each one, then get the weather in Austin, TX"
    )
    result = await Runner.run(agent, input=query)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())