from dotenv import dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dataclasses import dataclass


config = dotenv_values(".env")


model = init_chat_model("google_genai:gemini-2.5-flash-lite", google_api_key=config.get("GEMINI_API_KEY"))
checkpointer = InMemorySaver()

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# print(model.invoke("hello there"))
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return {"temperature":"30 degree celsius", "wind":"15 km/hour"}

agent = create_agent(
    model=model,
    system_prompt="You are a helpful assistant",
    tools=[get_weather],
    # checkpointer=checkpointer
)

# config = {"configurable": {"thread_id": "1"}}

for chunk in agent.stream(
    {"messages":[{"role":"user", "content":"what is the wether in kochi"}]},
    stream_mode="updates"
):
    for step, data in chunk.items():
        print("step : ", step)
        print("content", data['messages'][-1].content_blocks)
        print("\n")

# res = agent.invoke(
#     {"messages": [{"role": "user", "content": "my name is rashid"}]},
#     config = {"configurable": {"thread_id": "1"}},
#     context=Context(user_id="1")
# )

