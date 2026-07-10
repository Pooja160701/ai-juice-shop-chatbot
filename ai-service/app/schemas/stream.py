from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class ChatStreamRequest(BaseModel):
    messages: list[Message]