import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
email=input("Enter email:")
response=client.chat.complete(
model="mistral-small-latest",
    messages=[
        {
            "role":"system",
             "temperature":0.3,
            "content":"""you are an email classifier, you have to classifiy the email based on email recevied from the user"
            "example1":"the user will have to pay for dilevery, so category will be billing"
            "example2":"the user want urgently his id card back that he lost, so category will be urgent"
            "example3":"if user email for any general purpose, ctaegory will be general"
            "example4":"if any spam email then gategory will be spam mail"
            "so classify the email as urgent,billing,general or spam based on email recevied then write appropriate reply"
            "template":"email,category and reply"""
        },
        {
            "role":"user",
            "content":f"email{email}"

        },
    ]
)
print(response.choices[0].message.content)
