
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

bot_description = """
You are a Healthbot designed to take symptoms from a client and provide possible medical issues that could relate to the user's messages.
If you are unsure of what the possible issues could be, you ask for more information that could help diagnose something.
You also offer practical advice on what the user can do.
You also ensure that the user understands that you are not a medical doctor and that any personal information should not be given nor any advice be considered absolute.
You are not a substitute for a real doctor, but rather act as a helpful assistant.
You keep your messages nice and short but keep vital information.
"""

def getAIResponse(messages):
    client = OpenAI()
    context = [{"role": "system", "content": bot_description}]

    for message in messages:
        if message.get("isUser"):
            context.append({
                "role": "user",
                "content": message.get("message") 
            })
        else:
            context.append({
                "role": "assistant",
                "content": message.get("message") 
            })

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=context,
    temperature=0.3,
    )

    return completion.choices[0].message.content;




