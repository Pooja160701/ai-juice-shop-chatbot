from app.rag.generator import rag_generator


class ChatService:

    def ask(self, question: str):

        return rag_generator.ask(question)


chat_service = ChatService()