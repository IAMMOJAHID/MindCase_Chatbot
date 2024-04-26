
import streamlit as st
import time
from Model import read_pdf, get_answer_to_question

# with st.container():
    # st.title("Welcome To Medical Diagnosis Chatbot")
    # st.write("Note: This ChatBot is in developing face. Clearly input your problem (ChartBot may not recognize partial question)")

pdf_text = read_pdf("blade_runner_2049.pdf")

st.write(
    """
    <div>
        <h2 style="text-align: center;">Welcome To MindCase Chatbot</h2>
    </div>
    """,
    unsafe_allow_html=True
)


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

ModelOutput=""""""
def stream_data():
    for word in ModelOutput.split(" "):
        yield word + " "
        time.sleep(0.02)
        
        
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if(prompt=="""Hi""" or prompt=="""hi""" or prompt=="""Hello""" or prompt=="""hello"""):
            ModelOutput="""Hello"""
        else:
            ModelOutput, Generator=get_answer_to_question(pdf_text, prompt)

        response = st.write_stream(stream_data)
    st.session_state.messages.append({"role": "assistant", "content": response})
