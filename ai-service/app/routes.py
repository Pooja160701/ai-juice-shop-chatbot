from fastapi import APIRouter

from app.models import ChatRequest, ChatResponse
from app.services import ask_llm

router = APIRouter()


@router.post("/ask", response_model=ChatResponse)
def ask(request: ChatRequest):

    answer = ask_llm(request.message)

    return ChatResponse(response=answer)