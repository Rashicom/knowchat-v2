import streamlit as st
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

    # pass the prompt to llm as stream

    with st.chat_message("bot"):
        status_placeholder = st.empty()
        for stage in ["thinging","searching","content response"]:
            status_placeholder.markdown(stage)
            time.sleep(1)
        
        st.session_state.messages.append({"role":"bot", "content":stage})