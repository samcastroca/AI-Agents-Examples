# LangChain Console Agents Examples

A collection of LangChain agents that can be used from the command line.

## Project Structure

```
langchain-agents/
├── main.py                 # Main entry point (CLI)
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuration settings
├── agents/
│   ├── __init__.py
│   ├── base_agent.py      # Base agent class
│   ├── react_agent.py     # ReAct agent
│   ├── conversational_agent.py  # Conversational agent with memory
│   └── tool_agent.py      # Agent with custom tools
├── tools/
│   ├── __init__.py
│   └── custom_tools.py    # Custom tool definitions
└── utils/
    ├── __init__.py
    └── helpers.py         # Utility functions
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   copy .env.example .env
   ```

## Usage

Run the main script:
```bash
python main.py
```

Or select an agent directly:
```bash
python main.py --agent 1  # ReAct Agent
python main.py --agent 2  # Conversational Agent
python main.py --agent 3  # Tool Agent
```

## Available Agents

1. **ReAct Agent** - Uses reasoning and acting to solve tasks
2. **Conversational Agent** - Maintains conversation history for multi-turn interactions
3. **Tool Agent** - Can use custom tools to accomplish tasks

## Adding New Agents

1. Create a new file in `agents/`
2. Inherit from `BaseAgent`
3. Implement `create_agent()` and `run()` methods
4. Register in `main.py`

## Adding Custom Tools

Add new tools in `tools/custom_tools.py` using the `@tool` decorator.
