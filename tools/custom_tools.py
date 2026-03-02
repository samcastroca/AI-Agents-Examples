"""Custom tools for agents."""
from langchain.tools import tool
from tavily import TavilyClient
from typing import Any, Dict

tavily_client = TavilyClient()

@tool
def example_tool(query: str) -> str:
    """An example custom tool. Replace with your own implementation."""
    return f"Processed: {query}"


@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)