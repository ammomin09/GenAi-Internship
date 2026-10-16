import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
complaint=input("Enter customer complaint: ")
response=client.chat.complete(
model="mistral-small-latest",
messages=[
        {
            "role":"system",
            "content":"""you are a customer support agent for e-commerce company, you have to reply to the customer complaints in a professional and polite manner"
            "tone":"select tone automatically"
            "Understand customers even when they use broken, informal, or grammatically incorrect English. Do not criticize or correct their English. Reply in simple, clear, polite English that is easy to understand.”
            "You have to reply all customers complaints whether it is in formal or informal manner, you have to reply in a professional and polite manner and select tone automatically based on the complaint received from the customer"
            "and auto dectect if the complaint is angry or nuetral then pick the tone itself and aslo classify complaint severity then reply, max words 100"
            "template": customer complaint then your reply and according to tone complimentary close"
            "temperature=0.7"""
        },
        {
            "role":"user",
            "content":f"complaint: {complaint}"
        },
     ]

)
print(response.choices[0].message.content)

