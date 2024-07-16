from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message):
    # print(message.from_user)
    # await message.answer(f"Привет, {message.from_user.first_name}")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм",url="https://www.instagram.com/_sultanbekov_05/?next=%2F")
            ],
            [
             types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
              types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data = "donate_us")
            ]
        ]

    )
    await message.reply(f"Привет, {message.from_user.first_name}! Наш бот для покупок", reply_markup=kb)

@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Информация о нас')

@start_router.callback_query(F.data == "donate_us")
async def about_us_handler(callback: types.CallbackQuery):
    await callback.message.answer('Спасибо за пожертвование')