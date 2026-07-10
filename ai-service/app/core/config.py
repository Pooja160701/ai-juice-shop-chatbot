import os

from dotenv import load_dotenv

ENV_FILE = os.getenv("ENV_FILE", ".env.local")

load_dotenv(ENV_FILE)


class Settings:

    PROJECT_NAME = "Juice Shop AI Assistant"

    API_VERSION = "v1"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5-mini"
    )

    JUICE_SHOP_API = os.getenv("JUICE_SHOP_API")

    CHROMA_PATH = os.getenv(
        "CHROMA_PATH",
        "./chroma_db"
    )


settings = Settings()