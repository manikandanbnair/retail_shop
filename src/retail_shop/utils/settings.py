from pydantic_settings import BaseSettings,SettingsConfigDict

class PostgresSettings(BaseSettings):
    instance_name: str
    db_name: str
    db_user: str
    ip_type: str
        
    model_config = SettingsConfigDict(
        env_prefix= "DB_POSTGRES"
    )
class Settings(BaseSettings):
    env: str ="development"

    postgres_database: PostgresSettings = PostgresSettings()

    model_config = SettingsConfigDict(
        use_enum_values= True
    )