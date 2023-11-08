from aiogram import Dispatcher, Bot, types, executor

API_TOKEN = "6558256365:AAGwhETtCarQGeQSY8T6HwK1KCGNfFIk_Qo"
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot=bot)

@dispatcher.message_handler()
async def send_welcome(message: types.Message):
    await message.reply(text=message.text)

executor.start_polling(dispatcher=dispatcher)