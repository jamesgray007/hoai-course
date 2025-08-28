# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python-based educational repository for the "Hands-on AI for Leaders" course, focusing on building AI workflows and agents using various AI APIs and SDKs. The codebase is structured by week, with progressive topics from AI assistants to multi-agent systems.

## Development Commands

### Virtual Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Running Python Scripts
```bash
# General pattern for running scripts
python src/week-{n}/{platform}/{script_name}.py

# Examples
python src/week-3/openai/model-response.py
python src/week-4/openai/single-agent/single_agent.py
```

## Architecture

### Project Structure
- **src/week-1/**: Prompt engineering patterns and templates
- **src/week-2/**: AI workflows with assistants and no-code platforms
- **src/week-3/**: API integrations (OpenAI, Anthropic, Google, Perplexity) for building workflows
- **src/week-4/**: Agent implementations including single and multi-agent systems

### Key Dependencies
- **openai**: OpenAI API client
- **openai-agents**: OpenAI's agent SDK for building autonomous agents
- **python-dotenv**: Environment variable management
- **mcp**: Model Context Protocol for tool integration
- **httpx**: HTTP client for API requests

### Agent Architecture (Week 4)
The agent implementations follow these patterns:

1. **Single Agent Pattern** (src/week-4/openai/single-agent/):
   - Uses Agent class from openai-agents
   - Implements tools: WebSearchTool, FileSearchTool, FunctionTool, ImageGenerationTool
   - Instructions loaded from markdown files for maintainability

2. **Multi-Agent Pattern** (src/week-4/openai/multi-agent/):
   - **Handoff Pattern**: Agents transfer control based on specialization
   - **Deterministic Pattern**: Fixed agent workflows
   - **Agent-as-Tool Pattern**: Agents callable as tools by other agents

### Environment Configuration
Create a `.env` file in the root with:
```
OPENAI_API_KEY=your_key_here
VECTOR_STORE_ID=your_vector_store_id  # For file search capabilities
```

### Common Patterns in Code
- All scripts load environment variables using `python-dotenv`
- Async operations use `asyncio` for agent runners
- Agent instructions are stored in separate markdown files
- Output files are saved to `output/` directories with timestamps