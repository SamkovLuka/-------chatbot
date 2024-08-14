import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from dotenv import find_dotenv, load_dotenv
import os
from aiogram.types import Message
load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Hello user")


@dp.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer("I am your telegram bot and i will help you to make choice")
async def main():
    await dp.start_polling(bot)

@dp.message(F.text == "Hello")
async def answer_hello(message:Message):
    await message.reply(f"Hello, my friend {message.from_user.full_name}")

@dp.message(F.voice)
async def answer_voice(message:Message):
    await message.reply("This is voice message")


@dp.message(F.photo)
async def answer_photo(message: Message):
    await message.reply("This is photo")


@dp.message(F.text == "💯")
async def answer_100(message:Message):
    await message.reply(f"💯")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("end of work")
asyncio.run(main())