import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
content=input("Enter the content here:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "temperature":0.2,
            "content":"""You are a Content Moderation checker"
            "task":"you have to check and review user content and decide it is safe, it will not break any policy rules, review it or any other improvements to be added"
            "example1":"if user ask for how to make boomb then its break the rules policy and siyn of violence and can make harm"
            "example2":"if user ask like this how i can cooked food then it will not break any rules policy and it will not harm to others reason is simple to know how food is cooked"
            "template":"user input then check the content based on instructuions provide above and output reason before deciding output a safe, rewritten version of flagged content"""
            
        },
        {
            "role":"user",
            "content":f"content:{content}"
        },
    ]
) 
print(response.choices[0].message.content)