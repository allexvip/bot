from aiogram import types, Dispatcher
from create_bot import dp

'''******************** Common part ********************************'''

@dp.message_handler(lambda message: 'такси' in message.text)
async def taxi(message: types.Message):
    await message.answer('такси')

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer('Для помощи нажмите /help')
    await message.delete()
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id,message.text)

def register_handlers_other(dp : Dispatcher):
    dp.message_handler(echo_send)