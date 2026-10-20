import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
userdetails=input("Enter Your details:")
job=input("Enter job description:")
tone=input("Enter tone:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "content":"""You are professional career coach for the job seekers"
            "task":"you have to create a tailored professional resume cover letter for the candidates/user"
            "template":"must use 2 big variable user details and job description, according to it first match skills to job,"
            "then create a cover letter, structure should be totally professional"
            "temeparture":"0.5"""
        },
        {
            "role":"user",
            "content":f"details:{userdetails},job description:{job},tone:{tone}"
        },
    ]
)
print(response.choices[0].message.content)