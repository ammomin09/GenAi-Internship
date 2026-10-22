import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_PI_KEY"))
topic=input("Enter Topic:")
diff=input("Enter Difficulty level:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "temperature":0.6,
            "content":"""you are a professional teacher"
            "task":"you have to generate 5 quizs on user selected topic according to difficulty level"
            "template":"according to topic create 5 quizs multiple-choice questions+answers note that "
            "check each question is right step by step and format via few shot"""
        },
        {
            "role":"user",
            "content":f"Quiz Topic:{topic},Quiz Difficulty level:{diff}"
        },
    ]
)
print(response.choices[0].message.content)