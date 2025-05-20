from openai import OpenAI
import json
import requests
import os
from dotenv import load_dotenv

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key

load_dotenv() # this loads the environment variables from the .env file

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable

client = OpenAI(api_key=api_key)

# Custom function to get weather
# Uses open-meteo API - https://open-meteo.com/
def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&temperature_unit=fahrenheit")
    data = response.json()
    return data['current']['temperature_2m']

# Step 1: Call model with get_weather tool defined

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for provided coordinates in fahrenheit.",
    "parameters": {
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]

input_messages = [{"role": "user", "content": "What's the weather like in Austin, TX today?"}]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools,
)
# Step 2: Let's see the model response when deciding to call the get_weather tool
print(response.output)

# Step 3: Execute the get_weather tool
tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_weather(args["latitude"], args["longitude"])
# print the API response
print(result)

# Step 4: supply the model with the tool result to generate a final response in a friendly format
input_messages.append(tool_call)  # append model's function call message
input_messages.append({                               # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools,
)
#Step 5: Let's see the final response to the user question
print(response_2.output_text)
