import os
import streamlit as st
from dotenv import load_dotenv
from mistralai.client import Mistral
from mistralai.client.utils.retries import BackoffStrategy, RetryConfig

load_dotenv()
client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY"),
    retry_config=RetryConfig(
        strategy="backoff",
        backoff=BackoffStrategy(
            initial_interval=1000,
            max_interval=8000,
            exponent=2,
            max_elapsed_time=30000,
        ),
        retry_connection_errors=False,
    ),
)

st.title("Welcome To Study.Ai")
st.write("Study and learn easily")
user_input=st.text_area("Enter the topic")

if st.button("submit"):
    if not user_input.strip():
        st.warning("Please enter somthing...")
    else:
        with st.spinner("Processing..."):
            response=client.chat.stream(
                model="mistral-small-latest",
                temperature=0.7,
                messages=[
                    {
                        "role":"system",
                        "content":"you are a phd scholar in all domains in world wide, "
                        "you have to provide a proper formted output to user in points"
                    },
                    {
                        "role":"user",
                        "content":user_input
                    },
                ]
            )

            def token_stream():
                for chunk in response:
                    content=chunk.data.choices[0].delta.content
                    if content:
                        yield content

            st.write_stream(token_stream())
            user_input=" "