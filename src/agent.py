from langchain.agents import create_agent
from tools import get_user_location, get_weather_for_location, Context
from schema import ResponseFormat
from system_prompt import SYSTEM_PROMPT
from model import model
from memory import checkpointer

def build_agent():
    return create_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_user_location, get_weather_for_location],
        context_schema=Context,
        response_format=ResponseFormat,
        checkpointer=checkpointer,
    )
