<<<<<<< HEAD
from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo_handler(message):
    await message.answer("Я вас не понимаю, вот команды которые я понимаю: "
                         "/start - начало \n /myinfo - информация \n /random_recipe - рандомный рецепт \n "
                         "/feedback - Отзыв \n /menu"
=======
from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo_handler(message):
    await message.answer("Я вас не понимаю, вот команды которые я понимаю: "
                         "/start - начало \n /myinfo - информация \n /random_recipe - рандомный рецепт \n "
                         "/feedback - Отзыв \n /menu"
>>>>>>> 1effcec529a9b169037ec54dd4ba619df74afb77
    )