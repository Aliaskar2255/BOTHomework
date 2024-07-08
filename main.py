import asyncio
import logging
from BotConfig import bot, dp
from handlers.start import start_router
from handlers.Myinfo import my_info_router
from handlers.Recipe import recipe_router
from handlers.echo import echo_router
from handlers.dishes import dishes_router
async def main():
    # запуск бота
    dp.include_router(start_router)
    dp.include_router(my_info_router)
    dp.include_router(recipe_router)
    dp.include_router(dishes_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())