Бот для телеграм
===================
- в configs папке создать 2 файла:
    - .env (переменная TOKEN = p8usha;soi723roijwf)
            (TOKEN взять с телеграм BotFather)

    - config.py:
        from pydantic_settings import BaseSettings, SettingsConfigDict
        from pydantic import SecretStr
        from dotenv import load_dotenv

        class Settings(BaseSettings):
            load_dotenv()
            token: SecretStr
            model_config = SettingsConfigDict(env_file=".env",\
                                                env_file_encoding='utf-8')

        conf = Settings()
==================
Запуск производится через bot.py