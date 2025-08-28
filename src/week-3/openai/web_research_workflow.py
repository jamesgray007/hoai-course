"""
Simple web research workflow using OpenAI Responses API.

This script conducts web research on a user-provided topic using the
`web_search_preview` tool, summarizes findings, and saves a structured
markdown report to an `output/` directory.

Usage:
    python web_research_workflow.py "Impact of AI on cybersecurity in 2025"

Environment:
    - Set `OPENAI_API_KEY` in a `.env` file at the project root.

Author: James Gray
Last Updated: 2025-08-19
"""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI


def get_client() -> OpenAI:
    """Create and return an OpenAI client using environment variables.

    Returns:
        OpenAI: Configured OpenAI client.

    Raises:
        SystemExit: If the `OPENAI_API_KEY` is not set.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set. Create a .env file with your key.")
        raise SystemExit(1)
    return OpenAI(api_key=api_key)


def conduct_web_research(client: OpenAI, topic: str) -> str:
    """Use the Responses API with web search to research a topic.

    The model is instructed to perform multi-source web research and return a
    markdown-formatted report including a concise summary, key findings, and
    a list of sources as markdown links.

    Args:
        client (OpenAI): Initialized OpenAI client.
        topic (str): Topic to research.

    Returns:
        str: Markdown-formatted research report.

    Raises:
        Exception: If the API call fails.
    """
    instructions = (
        "You are a skilled research assistant. Search reputable, recent sources "
        "about the user's topic. Produce a clean markdown report with these "
        "sections: \n\n"
        "## Summary (150-250 words)\n"
        "Provide a concise, non-hallucinated synthesis.\n\n"
        "## Key Findings\n"
        "- 5-7 bullet points with concrete facts, metrics, or dates.\n\n"
        "## Sources\n"
        "- List 5-8 credible sources as markdown links in the form:"
        " [Title — Publisher] (URL) (Date if available)."
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        tools=[{"type": "web_search_preview"}],
        tool_choice="auto",
        input=f"Research topic: {topic}",
        instructions=instructions,
    )

    return response.output_text


def save_markdown(content: str, topic: str, output_dir: Optional[Path] = None) -> Path:
    """Save markdown content to a timestamped file.

    Args:
        content (str): Markdown content to write.
        topic (str): Topic string used to create a friendly filename.
        output_dir (Optional[Path]): Directory to save the file. Defaults to
            `src/week-3/responses-api/output/` next to this script.

    Returns:
        Path: Absolute path to the saved markdown file.
    """
    script_dir = Path(__file__).parent
    default_output = script_dir / "output"
    target_dir = output_dir or default_output
    target_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = "_".join(
        [p for p in "".join(ch if ch.isalnum() or ch in " -_" else " " for ch in topic).split()]
    )[:60]
    filename = f"web_research_{safe_topic}_{timestamp}.md" if safe_topic else f"web_research_{timestamp}.md"
    output_path = (target_dir / filename).resolve()

    header = f"# Web Research Report\n\n**Topic**: {topic}\n\n*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(content if content.endswith("\n") else content + "\n")

    return output_path


def main() -> None:
    """CLI entrypoint to run the web research workflow.

    Parses the topic from command-line arguments, conducts research using the
    Responses API, and writes a markdown report to the `output/` directory.

    Raises:
        SystemExit: On configuration or runtime errors.
    """
    parser = argparse.ArgumentParser(description="Web research to markdown using OpenAI Responses API")
    parser.add_argument("topic", type=str, help="Topic to research (wrap in quotes)")
    parser.add_argument(
        "--outdir",
        type=str,
        default=None,
        help="Optional output directory. Defaults to ./output next to this script.",
    )
    args = parser.parse_args()

    try:
        client = get_client()
        report_md = conduct_web_research(client, args.topic)
        outdir = Path(args.outdir) if args.outdir else None
        output_path = save_markdown(report_md, args.topic, outdir)
        print(f"Saved report to: {output_path}")
    except SystemExit:
        raise
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()


