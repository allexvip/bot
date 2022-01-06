import logging

from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram import executor

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_API_KEY'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)
    await bot.send_message(message.from_user.id,message.text)


executor.start_polling(dp,skip_updates=True)