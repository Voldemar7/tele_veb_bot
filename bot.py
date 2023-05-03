import asyncio

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import other_handlers, user_handlers
from database.database import user_base


# функція конфігурації і запуска бота
async def main():
    # загружаєм конфіг в змінну config
    config: Config = load_config()

    # ініціалізуєм бота і диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # реєструєм роутери в диспетчері
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропускаєм зібранні апдейти і запускаєм polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
