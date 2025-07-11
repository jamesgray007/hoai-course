# Import Python libraries we will use
import textwrap
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() # this loads the environment variables from the .env file

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable

# OpenAI Responses API with Web Search
# https://platform.openai.com/docs/api-reference/responses/create
client = OpenAI(api_key=api_key)

instructions = "Please provide a concise summary of the most significant AI news story from today."

# This function uses the OpenAI Responses API with Web Search
def webSearch (query: str) -> str:
    response = client.responses.create(
        model="gpt-4o",
        tools=[{"type": "web_search_preview"}],
        tool_choice="auto", #the model will decide which tool to use
        input=query,
        instructions=instructions
    )
    return response.output_text

raw_response = webSearch("What was a top AI news story from OpenAI?")
wrapped_response = textwrap.fill(raw_response, width=120)
print(wrapped_response)