import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()

client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
topic=input("Enter topic for post:")
platform=input("Enter Platform Names:")
tone=input("Enter tone for post:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
    {
        "role":"system",
        "temperature":0.3,
        "content":"""You are a Social media post creator"
        "platforms":"instagram,twitter,linkedin"
        "task":"You have to create social media post according to the topic,platform and tone recevied from the user"
        "template":"topic+paltform+tone, use platform specific format+tone control"""
        
    },
    {
        "role":"user",
        "content":f"topic:{topic},platform:{platform},tone:{tone}"
    },
    ]
)
print(response.choices[0].message.content)