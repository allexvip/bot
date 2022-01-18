from aiogram import types, Dispatcher
from create_bot import dp

'''******************** Common part ********************************'''
@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id,message.text)

def register_handlers_other(dp : Dispatcher):
    dp.message_handler(echo_send)