from aiogram import Router, types
echo_router = Router()

@echo_router.message()
async def echo_handler(message):
    await message.answer("Я вас не понимаю, вот команды которые я понимаю: "
                         "/start - начало \n /picture - картина"
                         )

