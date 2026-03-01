"""Main entry point for the LangChain Console Agents."""
import click
from rich.console import Console
from rich.prompt import Prompt

from utils.helpers import print_banner, print_response, print_error
from agents.react_agent import ReActAgent
from agents.conversational_agent import ConversationalAgent
from agents.tool_agent import ToolAgent

console = Console()

AGENTS = {
    "1": ("ReAct Agent", ReActAgent),
    "2": ("Conversational Agent", ConversationalAgent),
    "3": ("Tool Agent", ToolAgent),
}


@click.command()
@click.option("--agent", "-a", type=click.Choice(["1", "2", "3"]), help="Agent type to use")
def main(agent: str):
    """LangChain Console Agents - Interactive AI agents."""
    print_banner()

    # Select agent
    if not agent:
        console.print("\n[bold]Available Agents:[/bold]")
        for key, (name, _) in AGENTS.items():
            console.print(f"  {key}. {name}")
        agent = Prompt.ask("\nSelect an agent", choices=list(AGENTS.keys()))

    agent_name, agent_class = AGENTS[agent]
    console.print(f"\n[green]Selected:[/green] {agent_name}")

    # Initialize agent
    try:
        current_agent = agent_class()
        current_agent.create_agent()
    except Exception as e:
        print_error(f"Failed to initialize agent: {e}")
        return

    # Interactive loop
    console.print("\n[dim]Type 'quit' or 'exit' to stop, 'help' for commands[/dim]\n")

    while True:
        try:
            query = Prompt.ask("[bold cyan]You[/bold cyan]")

            if query.lower() in ["quit", "exit", "q"]:
                console.print("[yellow]Goodbye![/yellow]")
                break

            if query.lower() == "help":
                console.print("\n[bold]Commands:[/bold]")
                console.print("  quit/exit/q - Exit the program")
                console.print("  clear - Clear conversation (if supported)")
                console.print("  help - Show this help message\n")
                continue

            if query.lower() == "clear":
                if hasattr(current_agent, "clear_memory"):
                    current_agent.clear_memory()
                    console.print("[green]Memory cleared.[/green]")
                else:
                    console.print("[yellow]This agent doesn't support memory clearing.[/yellow]")
                continue

            # Run agent
            response = current_agent.run(query)
            if response:
                print_response(response)

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Goodbye![/yellow]")
            break
        except Exception as e:
            print_error(str(e))


if __name__ == "__main__":
    main()
