"""Conversational Agent implementation."""
from config import settings 
from typing import Any
from .base_agent import BaseAgent
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver  

class ConversationalAgent(BaseAgent):
    """Agent with memory for multi-turn conversations."""

    def __init__(self):
        super().__init__(
            name="Conversational Agent",
            description="An agent that maintains conversation history"
        )
        self.agent = None
        self.memory = None

    def create_agent(self) -> Any:
        """Create the conversational agent."""
        self.memory = InMemorySaver()
        self.agent = create_agent(model="gpt-5-nano",
                                  checkpointer=self.memory)

    def run(self, query: str) -> str:
        """Run the agent with a query."""
        config = {"configurable": {"thread_id": "1"}}
        question = HumanMessage(content=query)

        response = self.agent.invoke(
            {"messages": [question]},
            config=config
        )

        return response['messages'][-1].content

    def clear_memory(self):
        """Clear conversation history."""
        self.memory.delete_thread("1")