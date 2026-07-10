from app.prompts.rag_prompt import SYSTEM_PROMPT

from app.rag.retriever import product_retriever
from app.rag.formatter import context_formatter
from app.monitoring.metrics import OPENAI_REQUESTS

from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


class RAGGenerator:

    def ask(self, question: str):

        docs = product_retriever.retrieve(question)

        if not docs:

            return "I couldn't find that information in the Juice Shop catalog."

        context = context_formatter.build_context(
            docs
        )
        
        print("OpenAI completion called")
        OPENAI_REQUESTS.inc()

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""
Catalog

{context}

Question

{question}
""",
                },
            ],
        )

        return response.choices[0].message.content


rag_generator = RAGGenerator()