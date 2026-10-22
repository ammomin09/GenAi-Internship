import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
product=input("Enter product name:")
price=input("Enter price of product:")
discount=input("Enter discount:")
offer=input("Enter offer on products:")
response=client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role":"system",
             "temprature":0.8,
            "content":"""you are a marketing copywriter,you have to write marketing strategoies for the products and its feautures"
            "also display a shot tagline at the end of discription and generate 3 different discription"
            "template":"product name, product price, product discount and product offer, tagline display in proper formate"""
        },
        {
            "role":"user",
            "content":f"product name:{product},product price:{price},discount on product:{discount},offer:{offer} "
            "then your discription and tagline"

        },
    ]
)
print(response.choices[0].message.content)