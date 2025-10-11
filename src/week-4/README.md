# Week 4: Multi-Agent Systems

## Overview
This week focuses on designing and deploying autonomous agent systems using the OpenAI Agents SDK. You'll learn to build single agents and orchestrate multiple agents to work together on complex tasks.

## Learning Objectives
- Understand agent architecture and patterns
- Build single-agent systems with tools
- Design multi-agent systems with different orchestration patterns
- Implement handoffs between specialized agents
- Create deterministic agent workflows
- Use agents as tools for other agents
- Work with Model Context Protocol (MCP) for advanced integrations

## Prerequisites
- Completed Week 3 (API integration basics)
- Python 3.10+ with virtual environment activated
- Required packages installed:
  ```bash
  pip install openai openai-agents python-dotenv
  ```
- OpenAI API key in `.env`
- Vector Store ID for file search capabilities (optional)

## Week 4 Structure

### Single Agent Systems (`openai/single-agent/`)

Start here to understand the basics of agent architecture.

#### 1. **simple-simple-agent.py** - Minimal agent example
   - Bare-bones agent setup
   - Basic tool usage
   - Understanding agent responses
   ```bash
   python src/week-4/openai/single-agent/simple-simple-agent.py
   ```

#### 2. **single_agent.py** - Full-featured single agent
   - Web search capabilities
   - Instructions loaded from markdown files
   - Async execution with Runner
   - Multiple tool integration
   ```bash
   python src/week-4/openai/single-agent/single_agent.py
   ```

#### 3. **agent_instructions.md** - Externalizing instructions
   - Separating configuration from code
   - Maintainable instruction management
   - Best practices for agent prompts

### Multi-Agent Systems (`openai/multi-agent/`)

#### Pattern 1: Handoff Pattern
**File:** `multi_agents_handoffs.py`

Agents pass control to specialized agents based on request analysis.

**Use Case:** Customer service routing
- Triage agent analyzes requests
- Routes to billing, technical, or account specialists
- Seamless handoffs maintain context

**Key Features:**
- Dynamic routing based on content
- Specialized agent expertise
- Context preservation across handoffs

```bash
python src/week-4/openai/multi-agent/multi_agents_handoffs.py
```

**Architecture:**
```
Customer Request
    ↓
Triage Agent (analyzes)
    ↓
    ├→ Billing Agent (payments, refunds)
    ├→ Technical Support (bugs, features)
    └→ Account Management (security, access)
```

#### Pattern 2: Deterministic Pattern
**File:** `deterministic.py`

Fixed sequential workflow where each agent's output feeds the next.

**Use Case:** Content creation pipeline
- Research agent → finds information
- Writer agent → summarizes and titles
- Publisher agent → formats as markdown

**Key Features:**
- Predictable execution order
- Clear data flow
- Easy to debug and maintain

```bash
python src/week-4/openai/multi-agent/deterministic.py
```

**Architecture:**
```
Query → Research Agent → Writer Agent → Publisher Agent → Output
```

#### Pattern 3: Agent-as-Tool Pattern
**File:** `agent_as_tools.py`

Agents are callable as tools by other coordinating agents.

**Use Case:** Complex task decomposition
- Coordinator agent manages overall workflow
- Specialist agents act as callable functions
- Flexible composition of capabilities

**Key Features:**
- Modular agent design
- Reusable agent components
- Dynamic agent selection

```bash
python src/week-4/openai/multi-agent/agent_as_tools.py
```

### Advanced Integrations

#### **mcptools.py** - Model Context Protocol integration
- Custom tool development
- MCP server connections
- Extended capabilities

#### **mcpzapier.py** - Zapier integration via MCP
- Connect to 5000+ apps
- Workflow automation
- External service integration

## Core Concepts

### Agent Architecture

```python
from agents import Agent, Runner

agent = Agent(
    name="agent_name",
    instructions="What the agent does and how",
    model="gpt-4o-mini",
    tools=[WebSearchTool(), FileSearchTool()],
    handoffs=[other_agent]  # For handoff pattern
)
```

### Key Components

1. **Agent**: The autonomous entity
   - Name and identity
   - Instructions (system prompt)
   - Model selection
   - Tool access
   - Handoff capabilities

2. **Tools**: Extend agent capabilities
   - `WebSearchTool()`: Real-time web search
   - `FileSearchTool()`: Vector store queries
   - `FunctionTool()`: Custom Python functions
   - `ImageGenerationTool()`: DALL-E integration

3. **Runner**: Executes agent workflows
   - Async execution
   - Context management
   - Result handling

### Execution Pattern

```python
async def main():
    result = await Runner.run(
        agent,
        input="User query or task"
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

## Design Patterns Comparison

| Pattern | Use Case | Complexity | Flexibility |
|---------|----------|------------|-------------|
| **Single Agent** | Focused tasks, simple workflows | Low | Limited |
| **Handoff** | Dynamic routing, customer service | Medium | High |
| **Deterministic** | Fixed pipelines, content creation | Low | Low |
| **Agent-as-Tool** | Complex tasks, reusable components | High | Very High |

## When to Use Each Pattern

### Single Agent
- Task is well-defined and focused
- Single area of expertise needed
- Simple tool usage required
- Example: "Search web and summarize results"

### Handoff Pattern
- Request type determines specialist needed
- Multiple areas of expertise
- Dynamic routing required
- Example: Customer service, IT helpdesk

### Deterministic Pattern
- Clear sequential steps
- Each step has distinct responsibility
- Predictable workflow
- Example: Research → Write → Publish

### Agent-as-Tool Pattern
- Complex task decomposition
- Need to reuse agents in different contexts
- Dynamic workflow generation
- Example: Project management, data analysis pipelines

## Best Practices

### 1. Agent Design
- **Clear instructions**: Be specific about role and behavior
- **Single responsibility**: Each agent has one main job
- **Tool selection**: Only include necessary tools
- **Testing**: Start simple, add complexity gradually

### 2. Instructions
- Store in separate markdown files for maintainability
- Include examples of good behavior
- Specify output format requirements
- Define handoff criteria clearly

### 3. Error Handling
```python
try:
    result = await Runner.run(agent, input=query)
    print(result.final_output)
except Exception as e:
    print(f"Agent execution failed: {e}")
```

### 4. Tracing and Debugging
```python
from agents import trace

with trace("workflow_name"):
    result = await Runner.run(agent, input=query)
```

### 5. Performance
- Use `gpt-4o-mini` for faster, cheaper operations
- Use `gpt-4o` for complex reasoning tasks
- Minimize tool calls where possible
- Cache results when appropriate

## Common Patterns

### Loading Instructions from Files
```python
def load_instructions(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

instructions = load_instructions("agent_instructions.md")
```

### File Search with Vector Stores
```python
from agents import FileSearchTool

agent = Agent(
    name="research_agent",
    tools=[FileSearchTool(
        vector_store_ids=[os.getenv("VECTOR_STORE_ID")]
    )]
)
```

### Creating Handoffs
```python
# Define specialist agents
billing_agent = Agent(name="billing", ...)
support_agent = Agent(name="support", ...)

# Create triage agent with handoffs
triage_agent = Agent(
    name="triage",
    instructions="Route to appropriate specialist...",
    handoffs=[billing_agent, support_agent]
)
```

## Troubleshooting

### Agent Not Using Tools
- Check tool configuration in agent definition
- Verify instructions mention tool usage
- Ensure API has tool access enabled

### Handoffs Not Working
- Check `handoff_description` is clear
- Verify handoff instructions in triage agent
- Test with explicit routing scenarios

### Vector Store Issues
- Confirm `VECTOR_STORE_ID` in .env
- Verify files uploaded to vector store
- Check vector store permissions

### Async Execution Errors
```python
# Always use asyncio.run for async main
if __name__ == "__main__":
    asyncio.run(main())
```

## Output and Results

Agents can produce various outputs:
- Text responses and summaries
- Generated markdown reports (see `output/` directory)
- Images and media files
- Structured data

Example output structure:
```
src/week-4/openai/multi-agent/output/
└── report.md
```

## Testing Your Agents

1. **Start Simple**: Test with basic queries first
2. **Verify Tools**: Confirm each tool works independently
3. **Check Handoffs**: Test routing logic with specific scenarios
4. **Monitor Costs**: Track API usage during development
5. **Iterate**: Refine instructions based on results

## Real-World Applications

### Customer Service
- Handoff pattern for routing inquiries
- Specialized agents for different departments
- File search for knowledge base integration

### Content Creation
- Deterministic workflow for consistent output
- Research → Write → Edit → Publish
- Quality control at each stage

### Data Analysis
- Agent-as-tool for flexible analysis
- Different agents for various data types
- Coordinated reporting

### Task Automation
- Single agent for focused automation
- MCP integration for external services
- Scheduled execution with monitoring

## Next Steps

After mastering Week 4:
- ✓ Build production-ready agent systems
- ✓ Design multi-agent architectures
- ✓ Integrate with external services via MCP
- → Deploy agents to automate real workflows
- → Scale to production with monitoring and logging

## Additional Resources

### Documentation
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [OpenAI Platform Docs](https://platform.openai.com/docs/)

### Course Files
- `openai-agent-designer.md` - Agent design framework
- `sports_car_agent_instructions.md` - Example instructions
- `web_search_agent_instruction.md` - Web search agent example

### Getting Help
- Run `python check_setup.py` from project root
- Review CLAUDE.md for development patterns
- Join course community on Maven
- Check example outputs in `output/` directories

## Quick Reference

### Single Agent Template
```python
import asyncio
from agents import Agent, Runner, WebSearchTool

agent = Agent(
    name="assistant",
    instructions="You are a helpful assistant...",
    model="gpt-4o-mini",
    tools=[WebSearchTool()]
)

async def main():
    result = await Runner.run(agent, input="Your query")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

### Multi-Agent Template
```python
# Define specialists
specialist1 = Agent(name="specialist1", ...)
specialist2 = Agent(name="specialist2", ...)

# Create coordinator
coordinator = Agent(
    name="coordinator",
    instructions="Route to appropriate specialist",
    handoffs=[specialist1, specialist2]
)

# Execute
result = await Runner.run(coordinator, input=query)
```

Happy building!
