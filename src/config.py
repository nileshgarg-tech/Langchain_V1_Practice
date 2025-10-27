import os
from dotenv import load_dotenv

load_dotenv()  # Loads all keys from .env

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
