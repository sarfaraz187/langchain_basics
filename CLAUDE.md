# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python project for building LangChain-based AI agents using OpenAI models. Uses `uv` as the package manager and Python 3.11.

## Commands

```bash
# Install dependencies
uv sync

# Run main entry point
uv run main.py

# Run a specific module directly
uv run src/my_basic_agent.py

# Lint and format
uv run ruff check .
uv run ruff format .
```

## Architecture

- **main.py** - Entry point that loads environment variables and imports/runs agents from `src/`
- **src/** - Agent modules:
  - `my_basic_agent.py` - Basic agent with structured output using Pydantic models
  - `agent_with_tools.py` - Agent with custom tools (e.g., `@tool` decorated functions)

## Key Patterns

- Agents are created via `langchain.agents.create_agent()` with model, system prompt, and optional tools/response format
- Custom tools use the `@tool` decorator from `langchain.tools`
- Structured outputs use Pydantic `BaseModel` classes passed as `response_format`
- Environment variables (API keys) loaded via `python-dotenv` from `.env` file

## Code Style

- Ruff for linting/formatting (line-length: 88)
- Import sorting enabled (isort rules)
