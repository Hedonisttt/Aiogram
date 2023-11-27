from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Добро пожаловать в магазин Кроссовок БИСМАРК!</b>", parse_mode='HTML')



@dp.message_handler()
async def answer(message: types.Message):
    await message.answer('Я Не Понимаю Тебя')





if __name__ == "__main__":
    executor.start_polling(dp)

