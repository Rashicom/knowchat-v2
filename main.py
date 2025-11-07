import streamlit as st
import time
from agent_config import agent
import time


st.header("KnowChat-V2")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    

if prompt := st.chat_input("what's up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role":"user", "content":prompt})

    with st.chat_message("bot"):
        status_placeholder = st.empty()
        # pass the prompt to llm as stream
        for chunk in agent.stream(
            {"messages":[{"role":"user", "content":prompt}]},
            {"configurable": {"thread_id": "1"}},
            stream_mode="updates"
        ):
            for step, data in chunk.items():
                data_content = data['messages'][-1].content_blocks[-1]

                if step == "model":
                    if data_content.get("type") == "tool_call":
                        status_placeholder.markdown("Calling tool...")
                    else:
                        status_placeholder.markdown(data_content.get("text"))
                        st.session_state.messages.append({"role":"bot", "content":data_content.get("text")})
                else:
                    status_placeholder.markdown("Thinking...")
                time.sleep(1)