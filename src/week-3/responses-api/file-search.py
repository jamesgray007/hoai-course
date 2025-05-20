# Import Python libraries we will use
import textwrap
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from rich import print_json

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key
# VECTOR_STORE_ID=your_vector_store_id

load_dotenv() # this loads the environment variables from the .env file

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable
vector_store_id = os.getenv("VECTOR_STORE_ID") # this gets the vector store ID from the environment variable

# OpenAI Responses API with Web Search
# https://platform.openai.com/docs/api-reference/responses/create
client = OpenAI(api_key=api_key)

prompt = "How can I manage my self-limiting beliefs?"

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store_id]
    }],
    include=["file_search_call.results"]
)
# Convert response to JSON to view the results
response_json = response.to_json()
print(response_json)
# Print the output text
print (response.output_text)