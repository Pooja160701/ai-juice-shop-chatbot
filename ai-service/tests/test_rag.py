from app.rag.generator import rag_generator

answer = rag_generator.ask(
    "Tell me about Banana Juice."
)

print(answer)