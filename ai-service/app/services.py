from openai import OpenAI

from app.core.config import settings
from app.prompts import SYSTEM_PROMPT

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_llm(question: str):

    response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content