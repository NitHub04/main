import openai
import streamlit as st

openai.api_key = st.secrets["api_secret"]

"""
# Welcome to St Barts Cardiology Chatbot!
Ask any questions below:

Note:
This app uses OpenAI's GPT-3 to generate answers and is for research purposes only.
This is not medical advice.
"""

chatbot_input = st.text_input(label='Ask your question below', placeholder='e.g. what is a pacemaker?...')

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chatbot_input,
    temperature=0.1,
    max_tokens=4000
)

st.button(label="Submit", help='press to ask your question', on_click=answer)

answer = 'BartsChatbot:'+response["choices"][0]["text"]
st.write(answer)
print(answer)

"""
Please email your feedback to bartshealth.bartsaf@nhs.net
"""
