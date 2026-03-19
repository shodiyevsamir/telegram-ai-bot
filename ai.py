import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_ai(message, history=None):
    messages = history if history else []
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
