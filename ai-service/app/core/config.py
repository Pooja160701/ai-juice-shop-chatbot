import os
from dotenv import load_dotenv

env_file = os.getenv("ENV_FILE")

if env_file and os.path.exists(env_file):
    load_dotenv(env_file)
elif os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env"):
    load_dotenv(".env")


class Settings:

    PROJECT_NAME = "Juice Shop AI Assistant"

    API_VERSION = "v1"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5-mini",
    )

    JUICE_SHOP_API = os.getenv("JUICE_SHOP_API")

    CHROMA_PATH = os.getenv(
        "CHROMA_PATH",
        "./chroma_db",
    )


settings = Settings()