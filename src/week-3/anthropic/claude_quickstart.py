"""
Claude API Quickstart Example

This script demonstrates the basic usage of the Anthropic Claude API to send
a message and receive a response. It's designed as a minimal example for
understanding the core concepts of the Messages API.

Key Concepts:
- Setting up the Anthropic client
- Creating a message with the Messages API
- Understanding request parameters (model, max_tokens, messages)
- Handling and displaying the API response

Prerequisites:
- Install required packages: pip install anthropic python-dotenv
- Set ANTHROPIC_API_KEY in your .env file

API Documentation: https://docs.claude.com/en/api/messages
"""

import anthropic
from dotenv import load_dotenv
import json

# Load environment variables from .env file
# This allows us to securely store the ANTHROPIC_API_KEY
load_dotenv()

# Initialize the Anthropic client
# The API key is automatically read from the ANTHROPIC_API_KEY environment variable
client = anthropic.Anthropic()

# Create a message using the Messages API
# This is the main method for interacting with Claude
message = client.messages.create(
    # Model: Specifies which Claude model to use
    # claude-haiku-4-5 is the fastest model with near-frontier intelligence
    # Other options: claude-sonnet-4-5, claude-opus-4
    model="claude-haiku-4-5",

    # Max Tokens: Maximum number of tokens Claude can generate in the response
    # 1 token ≈ 4 characters of English text
    # Must be at least 1; varies by model (Haiku 4.5 supports up to 64K)
    max_tokens=1000,

    # Messages: Array of conversation turns with user and assistant roles
    # Must alternate between user and assistant (starting with user)
    # Each message has a "role" and "content"
    messages=[
        {
            "role": "user",  # The message is from the user
            "content": "What should I search for to find the latest developments in renewable energy?"
        }
    ]
)

# Display the complete API response
# The message object contains:
# - id: Unique identifier for this message
# - type: Always "message"
# - role: Always "assistant" for responses
# - content: Array of content blocks (text, tool use, etc.)
# - model: The model that generated the response
# - stop_reason: Why the model stopped generating (e.g., "end_turn", "max_tokens")
# - usage: Token usage statistics (input_tokens, output_tokens)
print(json.dumps(message.model_dump(), indent=2))