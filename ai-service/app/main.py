from fastapi import FastAPI

from app.core.config import settings
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.middleware.exception_handler import generic_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from app.api.stream import router as stream_router
from app.api.health import router as health_router
from prometheus_client import make_asgi_app
from app.middleware.request_logger import RequestLoggerMiddleware

app = FastAPI(
    title="Juice Shop AI Assistant",
    description="Enterprise AI Assistant for OWASP Juice Shop",
    version="1.0.0",
    contact={
        "name": "Pooja",
        "url": "https://github.com/Pooja160701"
    }
)

app.include_router(chat_router)
app.include_router(health_router)
app.include_router(stream_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggerMiddleware)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metrics_app = make_asgi_app()

app.mount("/metrics", metrics_app)

@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
    }