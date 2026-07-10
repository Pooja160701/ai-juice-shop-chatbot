import json

from fastapi import APIRouter

from fastapi.responses import StreamingResponse

from app.schemas.stream import ChatStreamRequest

from app.rag.generator import rag_generator

router = APIRouter()

def stream_response(answer: str):

    words = answer.split()

    for word in words:

        payload = {
            "choices": [
                {
                    "delta": {
                        "content": word + " "
                    }
                }
            ]
        }

        yield f"data: {json.dumps(payload)}\n\n"

    yield "data: [DONE]\n\n"

@router.post("/rest/chat")
async def chat(request: ChatStreamRequest):

    question = request.messages[-1].content

    answer = rag_generator.ask(question)

    return StreamingResponse(
        stream_response(answer),
        media_type="text/event-stream",
    )