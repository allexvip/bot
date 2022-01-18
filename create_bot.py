from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = os.getenv('TELEGRAM_BOT_NAME')
BOT_ADMIN_CHATID = os.getenv('TELEGRAM_ADMIN_CHATID')
START_MESSAGE = os.getenv('START_MESSAGE')

bot = Bot(token=os.getenv('TELEGRAM_API_KEY'))
dp = Dispatcher(bot)
