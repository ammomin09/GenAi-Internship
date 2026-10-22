import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
role=input("Enter a job role:")
level=input("Enter difficulty level:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "temperature":0.6,
            "content":"""You are an professional technical interviewer"
            "task":"you have to generate a 5 question based on user inputs+ideal answer points"
            "template":"check user input step by step, role for job then difficulty level and based 
            on that generate 5 interveiw question and then separate it into technical/behavioural"""
           
        },
        {
            "role":"user",
            "content":f"job role:{role},difficulty level:{level}"
        },
    ]
)
print(response.choices[0].message.content)