# Week 3: AI Workflows with Code and Agent Foundations

## Overview
This week focuses on leveraging AI APIs to build advanced workflows using code. You'll learn to integrate with multiple AI platforms and create custom functions that extend AI capabilities.

## Learning Objectives
- Build AI workflows using the OpenAI Responses API
- Integrate web search and file processing capabilities
- Work with multiple AI providers (OpenAI, Google, Perplexity, Anthropic)
- Use Model Context Protocol (MCP) for tool integration
- Create custom functions to extend AI capabilities
- Generate images programmatically

## Prerequisites
- Python 3.10+ installed
- Virtual environment activated (`.venv`)
- OpenAI API key configured in `.env`
- Required packages installed (run `pip install -r requirements.txt`)

## Week 3 Structure

### OpenAI Examples (`openai/`)

#### Getting Started
Start with these files in order:

1. **model-response.py** - Basic API interaction
   - Simple request/response pattern
   - Understanding the Responses API
   - Working with instructions and prompts
   ```bash
   python src/week-3/openai/model-response.py
   ```

2. **custom-function.py** - Creating custom tools
   - Define custom functions for AI to use
   - Function calling patterns
   - Structured outputs

3. **workflow.py** - Multi-step workflows
   - Web search → Analysis → Content generation → Translation
   - Sequential processing pattern
   - Saving outputs to markdown
   ```bash
   python src/week-3/openai/workflow.py
   ```

#### Search and Research Capabilities

4. **web-search.py** - Web search integration
   - Using the web_search_preview tool
   - Real-time information retrieval
   - Search result processing

5. **web_research_workflow.py** - Advanced research pipeline
   - Automated web research
   - Information synthesis
   - Report generation

6. **file-search.py** - Working with vector stores
   - File search capabilities
   - Vector store integration
   - Document retrieval patterns

#### Creative Capabilities

7. **create_image.py** - Image generation
   - DALL-E integration
   - Image creation from prompts
   - Saving generated images

#### Advanced Integration

8. **responses-mcp.py** - Model Context Protocol
   - MCP tool integration
   - Extended capabilities
   - Custom tool development

### Other Platforms

#### Perplexity (`perplexity/`)
- **sonar_search.py** - Perplexity's Sonar search API
  - Alternative search provider
  - Real-time web information
  - Citation-based responses

#### Google (`google/`)
- See `google-adk-readme.md` for Google AI SDK setup and examples

#### Claude Code (`claude-code/`)
- See `claude-sdk-readme.md` for Anthropic Claude SDK integration

## Common Patterns

### 1. Environment Setup
All scripts follow this pattern:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### 2. Basic API Call
```python
from openai import OpenAI

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Your prompt here",
    instructions="System instructions here",
    tools=[]  # Add tools as needed
)

print(response.output_text)
```

### 3. Using Tools
```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=query,
    instructions=instructions,
    tools=[{
        "type": "web_search_preview"
    }],
    tool_choice="auto"
)
```

### 4. Saving Outputs
Outputs are saved to the `output/` directory:
```python
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{output_dir}/result_{timestamp}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
```

## Key Concepts

### Responses API
- Simple request/response interface
- Instructions guide behavior
- Tools extend capabilities
- Automatic tool orchestration

### Tools and Functions
- **Web Search**: Real-time information retrieval
- **File Search**: Document and knowledge base queries
- **Custom Functions**: Define your own capabilities
- **Image Generation**: Create images from text descriptions

### Workflow Design
1. **Sequential**: Steps execute in order (workflow.py)
2. **Parallel**: Multiple calls for efficiency
3. **Conditional**: Logic-based execution paths
4. **Iterative**: Loop until goal achieved

## Troubleshooting

### API Key Issues
```bash
# Check if .env file exists and has valid key
cat .env | grep OPENAI_API_KEY

# Test API key
python -c "from openai import OpenAI; import os; from dotenv import load_dotenv; load_dotenv(); print('Valid' if os.getenv('OPENAI_API_KEY') else 'Missing')"
```

### Package Issues
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt

# Check specific package
pip show openai
```

### Common Errors
- **401 Unauthorized**: Check API key in .env
- **429 Rate Limit**: Wait and retry, or upgrade plan
- **ImportError**: Activate virtual environment and install packages
- **FileNotFoundError**: Run from project root directory

## Best Practices

1. **Always use virtual environments** to isolate dependencies
2. **Store API keys in .env** never in code
3. **Add error handling** for API calls
4. **Save outputs** with timestamps for tracking
5. **Use meaningful instructions** to guide AI behavior
6. **Test with small examples** before scaling up
7. **Monitor API usage** to control costs

## Output Files
Scripts create output files in the `output/` directory:
- `linkedin_posts_*.md` - Generated social media content
- `web_research_*.md` - Research reports
- Generated images and other artifacts

## Next Steps
After completing Week 3:
- ✓ You can build multi-step AI workflows
- ✓ You understand API integration patterns
- ✓ You can work with different AI providers
- → Move to Week 4 to build autonomous agent systems

## Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [OpenAI Responses API Reference](https://platform.openai.com/docs/api-reference/responses)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- Course CLAUDE.md for development patterns

## Support
- Check the main README.md for setup instructions
- Run `python check_setup.py` from project root to validate setup
- Review docs/local_setup.md for environment configuration
- Join the course community on Maven for help
