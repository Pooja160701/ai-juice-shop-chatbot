from fastapi import APIRouter
import time

from app.rag.generator import rag_generator
from app.monitoring.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
)
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post(
    "/ask",
    response_model=ChatResponse,
)
def ask(request: ChatRequest):

    REQUEST_COUNT.inc()
    print(">>>>>>>> REQUEST COUNT INCREMENTED <<<<<<<<")

    start = time.time()

    try:
        answer = rag_generator.ask(request.message)
        return ChatResponse(response=answer)

    finally:
        REQUEST_LATENCY.observe(time.time() - start)