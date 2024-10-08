from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / "bot.env",
        env_file_encoding="utf-8",
    )
    BOT_TOKEN: str


env = Config()  # type: ignore
