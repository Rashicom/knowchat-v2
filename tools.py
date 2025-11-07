from langchain.tools import ToolRuntime
from langchain.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return {"temperature":"30 degree celsius", "wind":"15 km/hour"}