# LangChain First Agent: Modular Weather Assistant

A refined LangChain tutorial demonstrating modular agent architecture with tools, memory, and structured responses.

## 🚀 Features

- Modular design with separate modules for agents, tools, memory, and configuration
- Custom tools for location detection and weather retrieval
- Conversation memory using LangGraph checkpointers
- Structured response schemas with punny personality
- Runtime context passing for user-specific operations

## 📁 Project Structure

```
src/
├── agent.py          # Agent construction
├── config.py         # Environment setup
├── main.py           # Demo application
├── memory.py         # Conversation persistence
├── model.py          # LLM initialization
├── schema.py         # Response formats
├── system_prompt.py  # Agent instructions
└── tools.py          # Custom tool implementations
```

## 🛠 Installation

1. **Clone and setup**:
   ```bash
   git clone https://github.com/nileshgarg-tech/Langchain_V1_Practice.git
   cd Langchain_V1_Practice
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Environment**: Create `.env` with `ANTHROPIC_API_KEY=your_key`

## 🚀 Usage

```bash
python src/main.py
```

Example output:
```
User: what is the weather outside?
Agent: {
  "punny_response": "It's looking bright and sunny - talk about a 'ray' of hope!",
  "weather_conditions": "Always sunny in Florida!"
}
```

## 🏗 Architecture

- **Agent Flow**: User input → Tool selection → Tool execution → Response generation → Memory update
- **Key Components**: LangChain agent, LangGraph memory, custom tools with context, typed schemas

## 📚 Learning Concepts

- Modular agent construction
- Tool runtime context
- Structured responses with schemas
- Memory integration
- Environment management

## 🔧 Customization

Add tools in `tools.py`, modify schemas in `schema.py`, change models in `model.py`.

## 📋 Requirements

- Python 3.10+
- Anthropic API key
- Dependencies in `requirements.txt`

## 🤝 Contributing

Educational project for LangChain best practices.