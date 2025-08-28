import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

SONAR_API_KEY=os.environ.get("SONAR_API_KEY")

# Set up the API endpoint and headers
url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {SONAR_API_KEY}",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Define the request payload
payload = {
    "model": "sonar",
    "messages": [
        {"role": "user", "content": "What were the top AI news stories today"}
    ]
}

# Make the API call
response = requests.post(url, headers=headers, json=payload)

# Print the AI's response
# print(response.json()) # replace with print(response.json()["choices"][0]['message']['content']) for just the content

print(response.json()["choices"][0]['message']['content'])