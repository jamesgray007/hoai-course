import os
import json
from openai import OpenAI
from datetime import datetime

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def search_web(query):
    """
    Step 1: Search the web using OpenAI's Responses API
    """
    response = client.responses.create(
        query=query,
        model="gpt-4-turbo-preview",
        max_tokens=2000,
        temperature=0.7
    )
    return response.text

def analyze_results(search_results):
    """
    Step 2: Analyze the search results and structure them
    """
    response = client.responses.create(
        query=f"Analyze and structure the following information into clear sections with key points and insights:\n\n{search_results}",
        model="gpt-4-turbo-preview",
        max_tokens=2000,
        temperature=0.7
    )
    return response.text

def save_to_markdown(content, topic):
    """
    Step 3: Save the analyzed content to a markdown file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_{topic.replace(' ', '_')}_{timestamp}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Research: {topic}\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content)
    
    return filename

def main():
    # Get the search topic from user input
    topic = input("Enter the topic you want to research: ")
    
    print("\nStep 1: Searching the web...")
    search_results = search_web(topic)
    
    print("\nStep 2: Analyzing results...")
    analyzed_content = analyze_results(search_results)
    
    print("\nStep 3: Saving to markdown...")
    filename = save_to_markdown(analyzed_content, topic)
    
    print(f"\nResearch complete! Results saved to: {filename}")

if __name__ == "__main__":
    main()
