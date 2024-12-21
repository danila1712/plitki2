import asyncio
import logging
from aiogram import Bot, Dispatcher,types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)
TOKEN = "7518712903:AAG8nc3E8YQEsfc3076e3Az-yN8saPEsZPE"
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('Gleb'))
async def fun_gleb(message: types.Message):
    await message.answer("glebinkton = svintus")

@dp.message(Command('photogleba'))
async def get_photo(message: types.Message):
    url = 'загружено.jpg'
    image = FSInputFile(url)
    await message.answer_photo(photo=image, caption='глеб')

@dp.message(F.text == 'глебинктон' )
async def fun_gleb1(message: types.Message):
    await message.answer("https://t.me/glebm0nchez")

async def main():
    await dp.start_polling(bot)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Gleb'))
    builder.add(types.KeyboardButton(text='глебинктон'))
    builder.add(types.KeyboardButton(text='photogleba'))
    await message.answer(
        "здраствуй, я monchez_bot. Что мне выполнить?",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

if __name__ == "__main__":
    asyncio.run(main())
