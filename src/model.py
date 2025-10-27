from langchain.chat_models import init_chat_model
from config import ANTHROPIC_API_KEY

model = init_chat_model(
    "anthropic:claude-sonnet-4-5",
    temperature=0.5,
    timeout=10,
    max_tokens=1000,
    api_key=ANTHROPIC_API_KEY,  # uses key from .env
)
