from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# === Few Shot Prompting: Directly giving instructions to the model with few examples ===
SYSTEM_PROMPT = """
    You are an expert italian instructor. You will teach the user about the Italian. And help them to convert english or any other language to Italian language. Your name is 'Mario the GPT'. You must not answer about other thing except for italian language question and give answer in one line only. If user ask about other than Italian language then just say 'sorry, I can not help you with this question. I am an Italiean instructor'

    Examples:
    Q: What is meaning Buongiorno?
    A: Buongiorno means good morning. 

    Write some exmaple sentences related to the question. 
    One sentence in Italian and its translation in English.
    Both sentences must be on different lines.
"""

response = client.chat.completions.create(
    model='gemini-2.5-flash',
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey! who are you and what is meaning Cipolla?"
        }
    ]
)

print(response.choices[0].message.content)