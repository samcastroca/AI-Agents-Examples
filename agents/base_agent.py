"""Base agent class that all agents inherit from."""
from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """Base class for all LangChain agents."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def create_agent(self) -> Any:
        """Create and return the LangChain agent."""
        pass

    @abstractmethod
    def run(self, query: str) -> str:
        """Run the agent with a query and return the response."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
