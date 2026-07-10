from fastapi import APIRouter
from app.rag.generator import rag_generator

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.openai_service import (
    openai_service,
)

router = APIRouter()


@router.post(
    "/ask",
    response_model=ChatResponse,
)
def ask(request: ChatRequest):

    answer = rag_generator.ask(request.message)

    return ChatResponse(response=answer)