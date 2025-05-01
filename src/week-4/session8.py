import asyncio
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, WebSearchTool, FileSearchTool

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Define the agents
# The sports case research agent

NEW_SPORTS_CAR_AGENT_INSTRUCTIONS = """
### Operating Instructions for a “New-Sports-Car Research” LLM Agent
*(Give these verbatim to the agent’s `instructions` parameter.)*

---

#### 1. Clarify the Research Goal
- **Objective:** Identify production (or confirmed-for-production) sports cars first shown, announced, or released in the past **12 months** or scheduled for release within the next **18 months**.  
- **Deliverable:** A concise table (or JSON) containing **model name, manufacturer, announcement date, target on-sale date, key specs (engine / EV layout, horsepower, 0-60, MSRP), and citation list** for each car.

#### 2. Generate Focused Search Queries
Create at least **five** search strings that mix these elements:

| Element           | Examples                                     |
|-------------------|----------------------------------------------|
| Release timeframe | “2025”, “2024-2025”, “upcoming”, “just revealed” |
| Car type          | “sports car”, “supercar”, “performance coupe”, “roadster” |
| Context words     | “launch”, “press release”, “debut”, “first drive” |

*Example queries:*  
- `2025 sports car debut press release`  
- `new performance coupes announced 2024`  
- `upcoming roadsters 2025 horsepower`

#### 3. Execute Web Searches Systematically
1. **For each query** use the agent’s `WebSearchTool` (or equivalent) with  
   - `recency = 90 days` for breaking news,  
   - broader recency for established reviews.  
2. **Collect the top 10 URLs** per query.  
3. **De-duplicate links** (same host & model).

#### 4. Prioritize High-Credibility Sources
1. **Manufacturer domains** – official specs & pricing.  
2. **Tier-1 automotive publications** (Car and Driver, MotorTrend, Top Gear, Autocar).  
3. **Specialist EV/performance sites** if the car is electric/hybrid.  
4. **Major general-news outlets** only if they carry original interviews or embargo lifts.  
Flag rumor blogs/forums as *unverified*.

#### 5. Extract and Validate Key Facts
- Pull **model name, powertrain, horsepower, torque, 0-60, MSRP, on-sale date**.  
- Cross-check **≥ 2 independent sources**; note discrepancies.  
- Capture the **exact sentence or spec table** for citation.

#### 6. Watch for Red Flags & Pitfalls
- **Concept-only vehicles** → exclude unless production confirmed.  
- **Regional variants** (e.g., *Z NISMO* vs *Fairlady Z*).  
- **Electric “performance” SUVs** → exclude unless clearly a 2-door sports car.

#### 7. Structure the Output
Return **Markdown** (or JSON) like this:

~~~markdown
### New Sports Cars (as of {today’s date})

| Model           | Maker  | Announced | On-Sale | Key Specs                          | MSRP (USD) | Sources |
|-----------------|--------|-----------|---------|------------------------------------|------------|---------|
| GR Supra GRMN   | Toyota | Jan 2025  | Q3 2025 | 3.0 L TC I6, ~550 hp, 0-60 ≈ 3.2 s | $75 k*     | [1],[2] |
~~~
> *Use “TBD” if price not given; bracket numbers map to the citation list.*

#### 8. Provide Proper Citations
After the table, list all URLs `[1]`, `[2]`, … in order:  
*Site – Article Title (YYYY-MM-DD).* Adapt to any special citation syntax your framework needs.

#### 9. Summarize Insights (Optional)
Finish with 2-3 bullets on trends (e.g., **hybridization above 600 hp**, **MSRPs up 12 % YoY**).

#### 10. Completion Criteria
Stop when you have either  
- **10 unique models** that qualify, **or**  
- no additional qualifying cars after exhausting queries.

Return results and end the task—do **not** chat beyond that unless explicitly asked.

---
**End of agent instructions.**
"""

sports_car_agent = Agent(
    name="Sports Car Agent",
    instructions=NEW_SPORTS_CAR_AGENT_INSTRUCTIONS,
    tools=[WebSearchTool()],
    model="gpt-4o-mini"
)

summarize_agent = Agent(
    name="Summarize Agent",
    instructions="You are a summarize agent that will summarize the sports car agent's output.",
    model="gpt-4o-mini"
)

# This is the manager agent that will orchestrate the sports car agent
manager_agent = Agent(
    name="Manager Agent",
    instructions="You are a manager agent that will orchestrate the sports car agent.",
    model="gpt-4o-mini",
    tools=[
        sports_car_agent.as_tool(
            tool_name="search_for_sports_cars",
            tool_description="Search for sports cars"
        ),
        summarize_agent.as_tool(
            tool_name="summarize_sports_cars",
            tool_description="Summarize the sports car agent's output"
        )
    ]
)

async def main():

    # Run the manager agent
    with trace("Manager Agent"):
        manager_result = await Runner.run(
            manager_agent,
            input="Please find me the best sports car for living in Austin, TX, and summarize the results."
        )

    print(manager_result)

if __name__ == "__main__":
    asyncio.run(main())


    


