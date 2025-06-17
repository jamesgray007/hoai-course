# Install Python packages in the terminal
# pip install openai
# pip install rich
# pip install python-dotenv

# Import Python libraries we will use
import textwrap
from openai import OpenAI
import os
from dotenv import load_dotenv

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key

load_dotenv() # this loads the environment variables from the .env file

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable

# establish the OpenAI client
client = OpenAI(api_key=api_key) # this creates the OpenAI client

# This code using the OpenAI Responses API to generate a response to the prompt
# https://platform.openai.com/docs/api-reference/responses/create

prompt = "What is the capital of Texas?"

# This code using the OpenAI Responses API to generate a response to the prompt
response = client.responses.create(
  model="gpt-4o-mini",
  input=prompt,
  instructions="Please provide a concise answer and include one interesting historical fact about the capital.",
  tools=[] #no tools are needed for this prompt
  
)

print(response)
print(response.output_text)