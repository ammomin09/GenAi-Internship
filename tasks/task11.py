import os
from mistralai.client import Mistral
from dotenv import load_dotenv
load_dotenv()
client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
reviews=[]
for i in range(1,3):
    review=input(f"Enter review {i}:")
    reviews.append(review)
    add=" | ".join(reviews)
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
            "temperature":0.2,
            "content":"""You are review sentiment analyzer"
            "task":"you have to review all the user's reviews in professional way"
            "template":"first review all then classify each as positive/negative or nuetral"
            " based on user's reviews then overall summmary of what customers like/dislike use zero-shot and print at the end how many positive vs negative reviews"
            "example":"you had a good reviews and bad reviews so it classify as nuetral"""
            
        },
        {
            "role":"user",
            "content":f"customers reviews:{add}"
        },
    ]
)
print(response.choices[0].message.content)