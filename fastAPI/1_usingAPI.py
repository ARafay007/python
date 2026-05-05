from fastapi import FastAPI, Body
from ollama import Client

client = Client(
    host = "http://localhost:11434"
)

app = FastAPI()

@app.get("/")
def read_root():
    return "hello API"

@app.get("/contact-us")
def contact_us():
    return { "contact": "0981203981203" }

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky orange?',
  },
]

@app.post("/chat")
def chat(message: str=Body(..., description="The message")):
    response = client.chat("gemma:2b", messages=[
        # {
        #     "role": "system",
        #     "content": """
        #         Just add jahil on every silly question.

        #         For Eample:
        #         Q: Why cow has 6 legs?
        #         A: Cow does not has 6. It has has 4 legs. Jahil!   
                
        #     """
        # },
        {
            'role': "user",
            'content': message,
        },
    ])
    return { "response": response.message.content }