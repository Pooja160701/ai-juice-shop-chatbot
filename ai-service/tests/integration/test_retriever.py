from app.rag.retriever import product_retriever


def test_retrieve_products():

    results = product_retriever.retrieve(
        "Which juice has banana?"
    )

    assert isinstance(results, list)
    assert len(results) > 0