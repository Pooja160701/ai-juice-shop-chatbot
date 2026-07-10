from app.rag.retriever import product_retriever

results = product_retriever.retrieve(
    "Which juice has banana?"
)

print(results)