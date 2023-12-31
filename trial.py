import streamlit as st
from streamlit_chat import message
import llama


# Age, gender, and height input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25, step=1)
gender_options = ["Male", "Female", "Other"]
selected_gender = st.selectbox("Select your gender", gender_options)
height = st.number_input("Enter your height (in cm)", min_value=0, value=160, step=1)
sentence = f"{selected_gender.lower()} ,{age} years old and {height} cm tall."
# st.write(sentence)


def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

st.title("Llama2 Clarifai Tutorial")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)

for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")

if user_prompt:

    combined_prompt = f"{user_prompt} {sentence}"

    st.session_state.messages.append({"role": "user", "content": combined_prompt})
    message(combined_prompt, is_user=True)

    response = llama.get_response(combined_prompt)  # get response from llama2 API

    msg = {"role": "assistant", "content": response}
    st.session_state.messages.append(msg)
    message(msg["content"])



if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)
