from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# using Gemini AI API via Open AI

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": "Who are you? Explain to me how AI works in one line."
        }
    ]
)

print(response.choices[0].message.content)