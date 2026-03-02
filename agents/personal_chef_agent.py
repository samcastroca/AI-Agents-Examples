"""personal Chef Agent implementation."""
from typing import Any
from .base_agent import BaseAgent
from tavily import TavilyClient
from tools.custom_tools import web_search
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
class ChefAgent(BaseAgent):
    """Personal Chef Agent."""

    def __init__(self):
        super().__init__(
            name="Chef Agent",
            description="An agent that provides personalized cooking advice and recipes"
        )
        self.agent = None
        self.tools = None

    def create_agent(self) -> Any:
        """Create the Chef agent."""
        self.tools = [web_search]
        system_prompt = """

        You are a personal chef. The user will give you a list of ingredients they have left over in their house.

        Using the web search tool, search the web for recipes that can be made with the ingredients they have.

        Return recipe suggestions and eventually the recipe instructions to the user, if requested.

        """
        self.agent = create_agent(
            model="gpt-5-nano",
            tools=self.tools,
            system_prompt=system_prompt,
            checkpointer=InMemorySaver()
        )
        
    def run(self, query: str) -> str:
        """Run the agent with a query."""
        config = {"configurable": {"thread_id": "1"}}
        question = HumanMessage(content=query)

        response = self.agent.invoke(
            {"messages": [question]},
            config
        )

        print(response['messages'][-1].content)