import os
from dotenv import load_dotenv
from mistralai.client import Mistral

# Load API key
load_dotenv()
api_key = os.getenv("MASTER_KEY")

# Create client
client = Mistral(api_key=api_key)

# Ask question
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "user", "content": "What is AI?"}
    ]
)

# Print answer
print(response.choices[0].message.content)
