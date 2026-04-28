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
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first  PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The Sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finaly an OUTPUT (which is going to be displayed to the user).

    Ouput JSON Format:
    { 
        "step": "START" | "PLAN" | "OUTPUT",
        "content": "string"
    }

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { 
        "step": "PLAN", 
        "content": "Seems like user is interested in maths problem." 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "looking at the problem, we should solve this using BODMAS method" 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "The BODMAS is correct thing to be done here." 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "First we multipy by 3 * 5 which is 15" 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "Now the equation is 2 + 15 / 10" 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "We must perform divide that is 15 / 10  = 1.5" 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "Now the equation is 2 + 1.5" 
    }
    PLAN: { 
        "step": "PLAN", 
        "content": "Now finally lets perform  the add 3.5" 
    }
    OUTPUT: { 
        "step": "OUTPUT", 
        "content": "Great, we have solved and finally left with 3.5 as ans" 
    }
"""

response = client.chat.completions.create(
    model='gemini-2.5-flash',
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey! write a code to add n numbers in js"
        }
    ]
)

print(response.choices[0].message.content)