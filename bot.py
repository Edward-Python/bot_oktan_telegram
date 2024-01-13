import asyncio
import logging
import time

from aiogram import Bot, Dispatcher

from app.configs.config import conf
from app.handlers import router_kb

        
async def main():
    dp.include_router(router_kb)
    # удаляет команды (когда откл.бот)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def times():
    time_time = time.time()
    local_time = time.localtime(time_time)
    format_time = time.strftime("%m-%d | %H:%M", local_time)
    return format_time
        

if __name__ == "__main__":
    bot = Bot(token=conf.token.get_secret_value())
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"\nБот начал работу!\n   {times()}\n")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\nБот завершил работу!\n   {times()}\n")
