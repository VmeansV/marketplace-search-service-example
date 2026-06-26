from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5435/search_db"
    )
    kafka_bootstrap_servers: str = Field(
        default="localhost:9092",
        validation_alias=AliasChoices("KAFKA_BOOTSTRAP_SERVERS", "KAFKA_BROKERS"),
    )
    kafka_topic_ads: str = Field(
        default="ads", validation_alias=AliasChoices("KAFKA_TOPIC_ADS")
    )
    kafka_consumer_group: str = "search-service"
    ad_service_url: str = "http://localhost:8002"
