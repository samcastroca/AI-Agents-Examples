"""Configuration settings for the agents."""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-4"
DEFAULT_TEMPERATURE = 0.7

# Agent Settings
MAX_ITERATIONS = 10
VERBOSE = True
