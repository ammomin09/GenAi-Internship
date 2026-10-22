import os
import json
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
bus=input("Enter business:")
response=client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    response_format={"type":"json_object"},
    max_tokens=100,
    messages=[
        { 
            "role":"system",
            "content":"""you are professional business analyst"
            "fromat":"structure all outputs in json fromat:Business,important things, marketing"""
        },
        {
            "role":"user",
            "content":f"{bus}"
        },
    ]
)

#print(response.choices[0].message.content)
raw=response.choices[0].message.content
print(raw)
try:
    data=json.loads(raw)
    print(data)
except json.JSONDecodeError:
    print("error while prase to json..")