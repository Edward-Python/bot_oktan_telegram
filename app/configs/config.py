from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from dotenv import load_dotenv


class Settings(BaseSettings):
    token: SecretStr
    
    load_dotenv()
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')


conf = Settings()


SQDALCGEMY_URL="sqlite+pysqlite:///cto_oktan.db"