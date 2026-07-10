from app.rag.generator import rag_generator


def test_rag_generator():

    answer = rag_generator.ask(
        "Tell me about Banana Juice."
    )

    assert isinstance(answer, str)
    assert len(answer) > 0