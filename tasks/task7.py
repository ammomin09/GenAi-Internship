import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
Message=input("Enter message:")
language=input("Enter targeted language:")
tone=input("Enter tone:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "content":"""You are a professional message translator"
            "task":"you have to transalte the message in correct language and formality according to language and tone selected by the user"
            "template":"auto dectect the input language first,message,translated message"
            "temperature":"0.7"""
        },
        {
            "role":"user",
            "content":f"message:{Message}"
        },
    ]
)
print(response.choices[0].message.content)