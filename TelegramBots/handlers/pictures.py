from aiogram import Router, types
from aiogram.filters.command import Command


picture_router = Router()

@picture_router.message(Command('picture'))
async def picture_handler(message: types.Message):
    photo = types.FSInputFile('images/books2.jpg')
    await message.answer_photo(
        photo=photo,
        caption="Интересная книга"
    )



