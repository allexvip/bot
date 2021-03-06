from aiogram import types, Dispatcher
from create_bot import dp, bot, BOT_NAME, START_MESSAGE
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from db import sqlite_db

'''******************** Client part ********************************'''


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, START_MESSAGE, reply_markup=kb_client)
        await message.delete()
    except Exception as e:
        await message.reply('Общение с ботом через личные сообщения, напишите ему:\nhttps://t.me/{0}'.format(BOT_NAME))
        await bot.send_message(BOT_ADMIN_CHATID,
                               'Error:\n@{0} ({1})\n{2}\n\n{3}'.format(message.from_user.username, message.from_user.id,
                                                                       message.text, str(e)))


@dp.message_handler(commands=['Режим_работы'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ВС с 10:00 до 20:00')


@dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Скоро открытие') #,reply_markup=ReplyKeyboardRemove()


@dp.message_handler(commands=['Меню'])
async def menu_command(message : types.Message):
    await bot.send_message(message.from_user.id,'Мы предлагаем:', reply_markup = kb_client)
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.message_handler(command_start, commands=['start', 'help'])
    dp.message_handler(open_command, commands=['Режим_работы'])
    dp.message_handler(place_command, commands=['Расположение'])
    dp.message_handler(menu_command, commands=['Меню'])
