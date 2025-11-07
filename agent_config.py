from dotenv import dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from dataclasses import dataclass
from tools import get_weather
from langgraph.checkpoint.memory import InMemorySaver


config = dotenv_values(".env")
model = init_chat_model("google_genai:gemini-2.5-flash-lite", google_api_key=config.get("GEMINI_API_KEY"))

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str


agent = create_agent(
    model=model,
    system_prompt="You are a financial expert chatbot",
    tools=[get_weather],
    checkpointer=InMemorySaver()
)
