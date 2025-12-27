# langchain_basics

A starter template for getting started with LangChain and OpenAI. This project uses `uv` as the package manager for fast and reliable Python dependency management.

## 🚀 Features

- **LangChain Integration**: Pre-configured LangChain setup for building LLM applications
- **OpenAI Support**: Ready-to-use OpenAI integration via `langchain-openai`
- **Example Scripts**: Multiple examples demonstrating key LangChain concepts
- **UV Package Manager**: Fast, modern Python package management with `uv`
- **Environment Management**: Secure API key handling with python-dotenv

## 📋 Prerequisites

- Python 3.12 or higher
- An OpenAI API key (get one at [OpenAI Platform](https://platform.openai.com/api-keys))
- `uv` package manager (will be installed if not present)

## 🛠️ Setup

### 1. Install UV (if not already installed)

```bash
pip install uv
```

### 2. Clone the repository

```bash
git clone <your-repository-url>
cd langchain_basics
```

### 3. Install dependencies

```bash
uv sync
```

This will create a virtual environment and install all required dependencies including:
- `langchain` - The main LangChain library
- `langchain-openai` - OpenAI integration for LangChain
- `python-dotenv` - Environment variable management

### 4. Configure your OpenAI API key

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_actual_api_key_here
```

## 🏃 Running the Examples

### Main Example

Run the main starter script:

```bash
uv run main.py
```

### Additional Examples

The `examples/` directory contains multiple example scripts demonstrating different LangChain features:

#### Example 1: Simple Chat Completion
```bash
uv run examples/01_simple_chat.py
```
Demonstrates basic chat completion and conversation with context.

#### Example 2: Prompt Templates
```bash
uv run examples/02_prompt_templates.py
```
Shows how to use reusable prompt templates for different tasks.

#### Example 3: Chains
```bash
uv run examples/03_chains.py
```
Demonstrates LangChain Expression Language (LCEL) and chain composition.

#### Example 4: Streaming Responses
```bash
uv run examples/04_streaming.py
```
Shows how to stream responses from OpenAI for real-time output.

## 📚 Project Structure

```
langchain_basics/
├── .env.example          # Example environment variables file
├── .gitignore           # Git ignore rules
├── .python-version      # Python version specification
├── pyproject.toml       # Project dependencies and metadata
├── main.py              # Main starter script
├── examples/            # Example scripts
│   ├── 01_simple_chat.py
│   ├── 02_prompt_templates.py
│   ├── 03_chains.py
│   └── 04_streaming.py
└── README.md            # This file
```

## 🔑 Key Concepts Covered

- **Chat Models**: Interacting with OpenAI's chat models
- **Messages**: System, Human, and AI messages for context
- **Prompt Templates**: Reusable templates with variables
- **Chains**: Composing multiple steps with LCEL
- **Streaming**: Real-time token-by-token responses
- **Output Parsers**: Processing and formatting model outputs

## 📝 Usage Tips

1. **Start Simple**: Begin with `main.py` and `01_simple_chat.py` to understand basics
2. **Explore Templates**: Move to `02_prompt_templates.py` for reusable patterns
3. **Build Chains**: Use `03_chains.py` to learn composition
4. **Add Streaming**: Implement `04_streaming.py` for better UX

## 🔧 Development

### Adding Dependencies

To add new dependencies:

```bash
uv add package-name
```

### Updating Dependencies

To update all dependencies:

```bash
uv sync --upgrade
```

## 🤝 Contributing

Feel free to fork this repository and customize it for your needs. This is a starter template designed to be modified and extended.

## 📖 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [UV Documentation](https://github.com/astral-sh/uv)

## ⚠️ Important Notes

- Never commit your `.env` file or expose your API keys
- Monitor your OpenAI API usage to avoid unexpected costs
- The examples use `gpt-3.5-turbo` for cost efficiency; you can change to `gpt-4` if needed

## 📄 License

This is a starter template - use it however you'd like!

---

**Happy coding with LangChain! 🎉**