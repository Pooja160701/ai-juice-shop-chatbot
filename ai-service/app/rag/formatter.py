class ContextFormatter:

    def build_context(
        self,
        retrieved_docs,
    ):

        context = []

        for doc in retrieved_docs:

            context.append(doc["document"])

        return "\n\n".join(context)


context_formatter = ContextFormatter()