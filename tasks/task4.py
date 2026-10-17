import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
transcript=input("Enter a transcript here:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "content":"""You are an action items extractor ,you have to extract action items from transcript"
            "chain of thought":"first extract action itmes from transcript then reply with 2 lines of summary"
            "exapmle":"in company meeting it is decided to make new office at baroda and all production cost will be provided from "
            "company funds and last deadline will be 20/12/2026, so action items will be new office, where at baroda and deadline"
            "template":"note action items, then reply"
            "temperature":"0.2"""
        },
        {
            "role":"user",
            "content":f"transcript:{transcript}"
        },
    ]
)
print(response.choices[0].message.content)