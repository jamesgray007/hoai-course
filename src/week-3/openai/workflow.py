import os
import json
from datetime import datetime
from typing import Dict, List, Any
import openai
from dotenv import load_dotenv

# Save your API key in the .env file
# OPENAI_API_KEY=your_api_key

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def web_search(query: str) -> str:
    """
    Step 1: Conduct a web search using the Responses API
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a web search assistant. Search the web for the given query and return relevant information in a clear, concise format. Focus on the most recent and authoritative sources.",
        tools=[{
            "type": "web_search_preview"
        }],
        tool_choice="auto",
        input=query
    )
    return response.output_text

def evaluate_results(search_results: str) -> str:
    """
    Step 2: Evaluate the search results and extract key insights
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are an expert analyst. Evaluate the search results and extract key insights. Focus on identifying trends, patterns, and actionable information. Present your analysis in a structured format with clear sections.",
        input=f"Analyze these search results and provide key insights: {search_results}"
    )
    return response.output_text

def generate_linkedin_post(insights: str) -> str:
    """
    Step 3: Generate a LinkedIn post based on the insights
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a professional LinkedIn content creator. Create an engaging post based on the provided insights. Use a professional yet conversational tone. Include relevant hashtags and make the content shareable and valuable to a professional audience.",
        input=f"Create a professional LinkedIn post based on these insights: {insights}"
    )
    return response.output_text

def translate_to_spanish(text: str) -> str:
    """
    Step 4: Translate the LinkedIn post to Spanish
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a professional translator specializing in business and professional content. Translate the given text to Spanish while maintaining the professional tone, cultural nuances, and LinkedIn-specific language conventions. Ensure the translation is natural and idiomatic.",
        input=f"Translate this LinkedIn post to Spanish while maintaining the professional tone: {text}"
    )
    return response.output_text

def save_to_markdown(english_post: str, spanish_post: str, output_dir: str = "output") -> str:
    """
    Save both English and Spanish posts to a markdown file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/linkedin_posts_{timestamp}.md"
    
    # Create markdown content
    content = f"""# LinkedIn Posts

## English Version
{english_post}

## Spanish Version
{spanish_post}

*Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filename

def main(query: str) -> str:
    """
    Main workflow function that orchestrates all steps
    """
    try:
        # Step 1: Web Search
        print("Conducting web search...")
        search_results = web_search(query)
        
        # Step 2: Evaluate Results
        print("Evaluating search results...")
        insights = evaluate_results(search_results)
        
        # Step 3: Generate LinkedIn Post
        print("Generating LinkedIn post...")
        english_post = generate_linkedin_post(insights)
        
        # Step 4: Translate to Spanish
        print("Translating to Spanish...")
        spanish_post = translate_to_spanish(english_post)
        
        # Save to markdown
        print("Saving posts to markdown...")
        output_file = save_to_markdown(english_post, spanish_post)
        
        print(f"Workflow completed successfully! Output saved to: {output_file}")
        return output_file
        
    except Exception as e:
        print(f"Error in workflow: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    query = "Latest trends in artificial intelligence and machine learning"
    main(query)
