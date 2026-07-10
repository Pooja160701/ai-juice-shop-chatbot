from openai import OpenAI

from app.core.config import settings
from app.core.logging_config import logger

SYSTEM_PROMPT = """
You are the official AI assistant of OWASP Juice Shop.

Only answer questions related to:

- Products
- Pricing
- Reviews
- Shopping
- Orders
- Payments

Politely refuse unrelated questions.
"""

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class OpenAIService:

    def ask(self, question: str):

        logger.info("Sending request to OpenAI")
        
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        logger.info("OpenAI response received")

        return response.choices[0].message.content


openai_service = OpenAIService()