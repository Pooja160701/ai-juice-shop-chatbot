from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Juice Shop AI Assistant"
    API_VERSION: str = "v1"

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-5"

    JUICE_SHOP_API: str

    CHROMA_PATH: str = "./chroma_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()