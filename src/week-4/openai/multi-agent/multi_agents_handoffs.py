"""
This code shows how to implement routing in a multi-agent system using the OpenAI Agents SDK.

The routing agent is responsible for determining which agent should handle the user's request.

The orchestrator agent is responsible for coordinating the other agents.   

This example shows the routing pattern with handoffs.

"""
import asyncio
from agents import Agent, Runner, trace
from agents import FileSearchTool
import os

# Define specialized agents for different types of customer service requests
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
    
)

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
)

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
)

# Define the triage agent that will route requests using handoffs
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

async def handle_customer_request(customer_query: str):
    """Handle a customer service request by routing it through the triage agent."""
    with trace("Customer Service Request"):
        result = await Runner.run(
            triage_agent,
            input=customer_query
        )
    return result

async def main():
    # Example customer queries
    queries = [
        "I'm trying to update my credit card information but the system keeps rejecting it.",
        "I can't log into my account. It says my password is incorrect but I'm sure it's right.",
        "The application crashes every time I try to export my data to PDF. What's going on?",
        "I was double-charged for my monthly subscription. Can I get a refund?",
        "How do I enable two-factor authentication for my account?"
    ]
    
    for query in queries:
        print(f"\n{'='*50}\nCustomer Query: {query}")
        result = await handle_customer_request(query)
        print(f"\nFinal Response: {result.final_output}")
        print(f"{'='*50}\n")

if __name__ == "__main__":
    asyncio.run(main())

