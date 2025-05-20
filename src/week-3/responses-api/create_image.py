# Install Python packages in the terminal
# pip install openai

# Import Python libraries we will use
from openai import OpenAI
import os
from dotenv import load_dotenv

from openai import OpenAI
import base64

load_dotenv() # this loads the environment variables from the .env file

api_key = os.getenv("OPENAI_API_KEY") # this gets the OpenAI API key from the environment variable

client = OpenAI(api_key=api_key)

prompt = """
A professor teaching an AI course at UC Berkeley"
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024",
    ##background="transparent",
    quality="high",
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("output/myimage.png", "wb") as f:
    f.write(image_bytes)