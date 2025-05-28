# This code is an example of how to use the OpenAI Responses API with a Zapier MCP server.
# https://openai.github.io/openai-agents-python/mcp/
# This provides agents with access to any of the tools that are available in your Zapier MCP Server.
# This pattern works for any MCP server, not just Zapier.
# OpenAI Cookbook: https://cookbook.openai.com/examples/mcp/mcp_tool_guide

# Install Python packages in the environment where you are running this code.
# pip install openai
# pip install python-dotenv

# Import Python libraries we will use
from openai import OpenAI
import os
from dotenv import load_dotenv

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key
# ZAPIER_MCP_API_KEY=your_api_key # this is the API key for the Zapier MCP server

load_dotenv() # this loads the environment variables from the .env file

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable

# establish the OpenAI client
client = OpenAI(api_key=api_key) # this creates the OpenAI client
# get the personal email from the environment variable
personal_email = os.getenv("PERSONAL_EMAIL")

# This prompt will be sent to the OpenAI Responses API as a multi-step workflow.
prompt = f"Please search the web to research what Google announced at recent I/O conference. Summarize what you found in 200-300 words, email to {personal_email} and post on the Slack channel for my coworkers to see."

response = client.responses.create(
  model="gpt-4o-mini",
  input=prompt,
  instructions="You are a helpful assistant that can search the web, summarize contentemail results to a user, and post on a Slack channel. Execute all actions without asking for confirmation.",
  tools=[{
            "type": "mcp",
            "server_label": "zapier",
            "server_url": "https://mcp.zapier.com/api/mcp/mcp",
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {os.getenv('ZAPIER_MCP_API_KEY')}"
            },
        }
    ],
)
print(response.output_text)