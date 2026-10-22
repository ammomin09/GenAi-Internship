import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
code=input("Enter code snippet:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "temperature":0.3,
            "content":"""You are a senior code enginner of your company"
            "task":"you have to explain the entire code in simple english step by step with docstring/comments generation"
            "template":"code,explianation and docstring or comments"""
            
        },
        {
            "role":"user",
            "content":f"code:{code}"
        },
    ]
)
print(response.choices[0].message.content)