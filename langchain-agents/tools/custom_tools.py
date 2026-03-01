"""Custom tools for agents."""
from langchain.tools import tool


@tool
def example_tool(query: str) -> str:
    """An example custom tool. Replace with your own implementation."""
    return f"Processed: {query}"


# Add more custom tools here
