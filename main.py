import logging

from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram import executor

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_API_KEY'))
BOT_NAME = os.getenv('TELEGRAM_BOT_NAME')
BOT_ADMIN_CHATID = os.getenv('TELEGRAM_ADMIN_CHATID')
START_MESSAGE = os.getenv('START_MESSAGE')
dp = Dispatcher(bot)


'''******************** Client part ********************************'''
@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,START_MESSAGE)
        await message.delete()
    except Exception as e:
        await message.reply('Общение с ботом через личные сообщения, напишите ему:\nhttps://t.me/{0}'.format(BOT_NAME))
        await bot.send_message(BOT_ADMIN_CHATID, 'Error:\n@{0} ({1})\n{2}\n\n{3}'.format(message.from_user.username, message.from_user.id, message.text, str(e)))

@dp.message_handler(commands=['Режим_работы'])
async def command_start(message : types.Message):

'''******************** Admin part ********************************'''


'''******************** Common part ********************************'''


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id,message.text)


executor.start_polling(dp, skip_updates=True)