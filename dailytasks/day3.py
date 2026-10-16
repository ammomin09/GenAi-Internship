import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
m1=input("Enter marks of subject 1: ")
m2=input("Enter marks of subject 2: ")
m3=input("Enter marks of subject 3: ")
m4=input("Enter marks of subject 4: ")
m5=input("Enter marks of subject 5: ")
total=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
percentage=(total/500)*100
grade=""
response=client.chat.complete(
model="mistral-small-latest",
messages=[
        {
            "role":"system",
            "content":"""You are a result calculator, you will have to calculate the total marks and percentage of the student"
            "and allow the grade based on the percentage got by the student. answer straight forward answer to the user question"
            "grading criteria: A+: 90-100, A: 80-89, B+: 70-79, B: 60-69, C: 50-59, PassClass: 40-49, Fail: below 40, and suggest the student to work hard if the student got fail grade or marks below 50%"""
        },
        {
            "role":"user",
            "content":f" Total Marks:{total} , Percentage: {percentage:.2f}%, Grade: {grade}"
        },

    ]

)
print(response.choices[0].message.content)

