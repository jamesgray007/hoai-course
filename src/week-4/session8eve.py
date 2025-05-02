import asyncio
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, WebSearchTool, FileSearchTool

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Define the agents

AGENT_INSTRUCTIONS = """
You are an **AI Web-Research Agent**.  
Your mission is to discover the **current top frameworks & tools for building AI agents**, then rank and summarize them for decision makers.  
Work with rigor, cite your sources, and produce a concise, structured output.

────────────────────────────────────────
A. SEARCH STRATEGY
────────────────────────────────────────
1. Run *at least three* distinct web-search queries that combine:
   • core concept : "AI agent framework", "agentic AI tooling", "LLM agent SDK", "autonomous agent library"  
   • freshness   : "2024", "2025", "latest", "new release", "GitHub"  
   • popularity  : "stars", "community", "production use"  
   Example queries  
     - top AI agent frameworks 2025 GitHub stars  
     - open-source LLM agent libraries popularity  
     - enterprise autonomous agent platform comparison

2. Harvest the first **20 unique** candidate frameworks/tools.  
   • Capture name, official URL (GitHub or docs), a one-sentence self-description, and *all* reference URLs you inspected.  
   • Discard duplicates and thin wrappers that simply re-export another framework.

────────────────────────────────────────
B. METADATA COLLECTION
────────────────────────────────────────
For each candidate, gather these **metrics** (public sources only):
   • **GitHub Stars**   : numeric count  
   • **Last Commit Date** : ISO-8601 (YYYY-MM-DD)  
   • **License**      : MIT, Apache-2.0, proprietary, etc.  
   • **Core Language(s)** : Python, TypeScript, Rust, etc.  
   • **Notable Integrations**: LangChain, OpenAI Agents SDK, RAG, vector DBs …  
   • **Primary Use Cases** : multi-tool RAG agents, workflow orchestration, autonomous research …  
   • **Community Signals** : Discord/Slack size, recent talks, StackOverflow tag activity, blog traction.

────────────────────────────────────────
C. RANKING RULES
────────────────────────────────────────
1. **Eligibility Filter** – keep only projects that:  
   • Had ≥1 commit in the last 6 months **OR** a clearly dated 2025 release note.  
   • Provide documentation beyond a README.  
   • Offer a permissive license *or* a transparent commercial model.

2. **Score** each remaining project on a 0-100 scale:  
   | Wt | Criterion                  | Guide |
   |---:|----------------------------|-------|
   | 35 | *Adoption* – GitHub stars (log-scaled), Discord size, prod users |
   | 25 | *Momentum* – commit recency & release cadence |
   | 20 | *Capability Depth* – built-in tools, multi-agent orchestration, extensibility |
   | 10 | *Docs & DX* – tutorials, type hints, tests |
   | 10 | *License Friendliness* – MIT/Apache > copyleft > closed |

3. **Rank** descending by total score; break ties by larger Momentum subtotal.

────────────────────────────────────────
D. SUMMARY OUTPUT
────────────────────────────────────────
Return a **JSON array** named `frameworks`, each element:

{
  "rank": 1,
  "name": "CrewAI",
  "score": 87,
  "url": "https://github.com/joaomdmoura/crewai",
  "one_liner": "Python library for orchestrating interconnected LLM ‘crew’ agents.",
  "key_metrics": {
    "github_stars": 9800,
    "last_commit": "2025-04-12",
    "license": "MIT"
  },
  "highlights": [
    "Supports OpenAI Agents SDK & task-tree orchestration",
    "Native RAG + vector-DB abstractions",
    "Active Discord (~8 k members) & weekly releases"
  ],
  "caveats": [
    "Limited non-Python language support",
    "Enterprise SLA only via paid tier"
  ],
  "citations": [
    "https://github.com/joaomdmoura/crewai",
    "https://blog.example.com/crewai-2025-review"
  ]
}

Return **only** this array (or `{ "frameworks": [], "message": "No qualifying frameworks found." }`).

────────────────────────────────────────
E. STYLE & VERIFICATION
────────────────────────────────────────
• Keep **`one_liner` ≤ 22 words**; plain English, no hype.  
• Use bullet fragments (∙) inside *highlights* & *caveats* if you must line-wrap.  
• Include **≥2 citations** per framework: the official repo **and** one reputable third-party source.  
• Validate all JSON with a linter before final output.  
• Never output extra keys or commentary outside the specified JSON.

────────────────────────────────────────
F. ETHICS & CURRENCY
────────────────────────────────────────
• Do **not** output private or pay-walled data.  
• Prefer sources dated **2024-07-01 or later** for relevance.  
• Flag obvious security concerns or abandoned repos in *caveats*.  
• If a framework’s license or maintenance status is unclear, mark it explicitly in *caveats*.

End of instructions.
"""

# Define the agents

web_search_agent = Agent(
    name="Web Search Agent",
    instructions=AGENT_INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[WebSearchTool()]
)

summarize_agent = Agent(
    name="Summarize Agent",
    instructions="You are a summarize agent that will summarize the web search agent's output.",
    model="gpt-4o-mini"
)

# Manager agent

manager_agent = Agent(
    name="Manager Agent",
    instructions="You are a manager agent that will orchestrate the web search agent and summarize agent.",
    model="gpt-4o",
    tools=[
        web_search_agent.as_tool(
        tool_name="web_search",
        tool_description="Search the web for the latest information on AI agent frameworks"
    ),
        summarize_agent.as_tool(
        tool_name="summarize",
        tool_description="Summarize the web search agent's output"
    )]
)

async def main():
    # Run the manager agent
    with trace("Manager Agent"):
        manager_result = await Runner.run(
            manager_agent,
            input="Please recommend the best tool for building AI agent in 2025 and beyond"
        )

    print(manager_result)

if __name__ == "__main__":
    asyncio.run(main())




