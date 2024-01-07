import asyncio
import logging

from aiogram import Bot, Dispatcher

from app import conf
from app import handlers


class BotRun:
        
    async def main(self):
        bot = Bot(token=conf.token.get_secret_value())
        dp = Dispatcher()
        dp.include_router(handlers.router)
        # удаляет команды (когда откл.бот)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        

if __name__ == "__main__":
    bot_run = BotRun()
    logging.basicConfig(level=logging.INFO)
    try:
        print("\nБот начал работу!\n")
        asyncio.run(bot_run.main())
    except:
        print('========================')
        print("\nБот завершил работу!\n")
        KeyboardInterrupt()
