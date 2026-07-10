from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "chat_requests_total",
    "Total chat requests"
)

REQUEST_LATENCY = Histogram(
    "chat_request_latency_seconds",
    "Chat request latency"
)

OPENAI_REQUESTS = Counter(
    "openai_requests_total",
    "OpenAI API calls"
)

RAG_SEARCHES = Counter(
    "rag_search_total",
    "Retriever searches"
)

EMBEDDING_REQUESTS = Counter(
    "embedding_requests_total",
    "Embedding API calls"
)