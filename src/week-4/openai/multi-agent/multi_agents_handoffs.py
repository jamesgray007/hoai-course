"""
OpenAI Multi-Agent System - Handoff Pattern

This script demonstrates the handoff pattern in multi-agent systems using the OpenAI 
Agents SDK. In this pattern, agents pass control to each other when they determine 
another agent is better suited to handle a specific request.

The system includes:
- Billing Agent: Handles payment issues, subscriptions, and refunds
- Technical Support Agent: Manages product troubleshooting and bug reports  
- Account Management Agent: Processes account access and security concerns
- Triage Agent: Routes customer inquiries to appropriate specialists

Key Features:
- Intelligent request routing based on content analysis
- Seamless handoffs between specialized agents
- File search capabilities for knowledge base integration
- Professional customer service workflow

Requirements:
- OpenAI API key
- Vector store ID for file search capabilities
- Python 3.10+
- Python virtual environment (.venv)
- Python libraries: openai, openai-agents, python-dotenv

Setup:
1. Create a new virtual environment (.venv)
2. Install required Python libraries: pip install openai openai-agents python-dotenv
3. Create a .env file with your OpenAI API key and vector store ID:
   - OPENAI_API_KEY=your_openai_api_key
   - VECTOR_STORE_ID=your_vector_store_id
4. Upload relevant documents to your OpenAI vector store for knowledge base

References:
- OpenAI Agents Documentation: https://openai.github.io/openai-agents-python/
- OpenAI Vector Stores: https://platform.openai.com/docs/assistants/tools/file-search

Author: James Gray
Last Updated: 2024-12-24
"""

# =====================================================================================
# DEPENDENCIES  
# =====================================================================================
# Install these Python libraries into virtual environment (.venv) using Terminal:
#   pip install openai          # OpenAI Python library for AI model interactions
#   pip install openai-agents   # OpenAI Agents framework for multi-agent systems
#   pip install python-dotenv   # Environment variable management

# =====================================================================================
# IMPORTS
# =====================================================================================
# Standard library imports
import asyncio
import os

# Third-party imports  
from dotenv import load_dotenv

# OpenAI Agents framework imports
from agents import Agent, Runner, trace, FileSearchTool

# =====================================================================================
# CONFIGURATION
# =====================================================================================
# Load environment variables from .env file
# Your .env file should contain:
# OPENAI_API_KEY=your_openai_api_key
# VECTOR_STORE_ID=your_vector_store_id
load_dotenv()

# =====================================================================================
# AGENT DEFINITIONS
# =====================================================================================
# Define specialized agents for different types of customer service requests

# Billing specialist agent for financial inquiries
billing_agent = Agent(
    name="billing_agent",
    instructions="""You are a billing specialist who handles:
    - Payment issues
    - Subscription questions
    - Refund requests
    - Billing cycle inquiries
    
    Always be professional and precise with financial matters.
    Provide clear explanations about billing policies.
    Ask for necessary information to resolve billing issues efficiently.""",
    model="gpt-4o-mini",
    tools=[FileSearchTool(vector_store_ids=[os.getenv("VECTOR_STORE_ID")])],
    handoff_description="Handoff to the billing agent for billing issues."
)

# Technical support specialist agent for product issues
technical_support_agent = Agent(
    name="technical_support_agent",
    instructions="""You are a technical support specialist who handles:
    - Product troubleshooting
    - Installation issues
    - Bug reports
    - Feature questions
    
    Provide clear step-by-step solutions when possible.
    Ask about the customer's device, software version, and recent actions.
    Be patient and thorough in your explanations.""",
    model="gpt-4o-mini",
    tools=[FileSearchTool(vector_store_ids=[os.getenv("VECTOR_STORE_ID")])],
    handoff_description="Handoff to the technical support agent for technical issues."
)

# Account management specialist agent for security and access issues
account_management_agent = Agent(
    name="account_management_agent",
    instructions="""You are an account management specialist who handles:
    - Account access issues
    - Profile updates
    - Security concerns
    - Account settings
    
    Prioritize account security and verification.
    Always verify the identity of the customer before making account changes.
    Explain the importance of security measures when implementing changes.""",
    model="gpt-4o-mini",
    tools=[FileSearchTool(vector_store_ids=[os.getenv("VECTOR_STORE_ID")])],
    handoff_description="Handoff to the account management agent for account management issues."
)

# Triage agent that routes requests using handoffs
triage_agent = Agent(
    name="customer_service_triage",
    instructions="""You are the initial customer service contact who routes customer inquiries to the appropriate specialist.
    
    Analyze the customer's request carefully and route to the most appropriate specialist:
    
    - For billing, payments, subscriptions, refunds → handoff to the billing_agent
    - For technical issues, bugs, product features → handoff to the technical_support_agent
    - For account access, security, profile management → handoff to the account_management_agent
    
    Before handing off to a specialist:
    1. Briefly acknowledge the customer's issue
    2. Explain that you're connecting them with the appropriate specialist
    3. Make your handoff decision based on the core issue, not peripheral details
    
    If unsure which specialist is needed, ask clarifying questions before making a handoff.""",
    model="gpt-4o-mini",
    handoffs=[billing_agent, technical_support_agent, account_management_agent]
)


# =====================================================================================
# CORE WORKFLOW FUNCTIONS
# =====================================================================================
async def handle_customer_request(customer_query: str):
    """Handle a customer service request by routing it through the triage agent.
    
    This function processes customer inquiries using the handoff pattern where
    the triage agent analyzes the request and hands off control to the most
    appropriate specialist agent based on the content and nature of the query.
    
    Args:
        customer_query (str): The customer's service request or inquiry that needs
            to be processed and routed to the appropriate specialist agent.
    
    Returns:
        Any: The result object from the agent execution containing the final
            response and any intermediate outputs from the handoff process.
    
    Raises:
        Exception: If there's an error during agent execution or handoff process.
        EnvironmentError: If required environment variables (like VECTOR_STORE_ID)
            are missing or invalid.
    """
    with trace("Customer Service Request"):
        result = await Runner.run(
            triage_agent,
            input=customer_query
        )
    return result


# =====================================================================================
# MAIN EXECUTION FUNCTION
# =====================================================================================
async def main():
    """Execute the multi-agent handoff workflow with sample customer queries.
    
    This function demonstrates the handoff pattern by processing various types
    of customer service requests. Each query is routed through the triage agent
    which determines the most appropriate specialist and hands off control.
    
    The function processes multiple example queries to showcase different routing
    scenarios including billing issues, technical problems, and account management
    concerns. Results are displayed to demonstrate the handoff workflow.
    
    Args:
        None
        
    Returns:
        None
        
    Raises:
        Exception: If there's an error during agent execution or query processing.
        EnvironmentError: If required environment variables are missing.
    """
    # Example customer queries demonstrating different routing scenarios
    queries = [
        "I'm trying to update my credit card information but the system keeps rejecting it.",
       # "I can't log into my account. It says my password is incorrect but I'm sure it's right.",
       # "The application crashes every time I try to export my data to PDF. What's going on?",
       # "I was double-charged for my monthly subscription. Can I get a refund?",
       # "How do I enable two-factor authentication for my account?"
    ]
    
    # Process each query and display results
    for query in queries:
        print(f"\n{'='*50}\nCustomer Query: {query}")
        try:
            result = await handle_customer_request(query)
            print(f"\nFinal Response: {result.final_output}")
        except Exception as e:
            print(f"\nError processing query: {e}")
        print(f"{'='*50}\n")


# =====================================================================================
# SCRIPT EXECUTION
# =====================================================================================
if __name__ == "__main__":
    asyncio.run(main())

