"""Helper utilities for the console application."""
from rich.console import Console
from rich.panel import Panel

console = Console()


def print_banner():
    """Print the application banner."""
    console.print(Panel.fit(
        "[bold blue]LangChain Console Agents[/bold blue]\n"
        "[dim]Interactive AI agents at your fingertips[/dim]",
        border_style="blue"
    ))


def format_response(response: str) -> str:
    """Format agent response for display."""
    return response.strip()


def print_response(response: str):
    """Print a formatted response."""
    console.print(Panel(response, title="Agent Response", border_style="green"))


def print_error(message: str):
    """Print an error message."""
    console.print(f"[bold red]Error:[/bold red] {message}")
