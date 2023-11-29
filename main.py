from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Связь')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Связь').add('Админ-Панель')

admins_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admins_panel.add('Статистика').add('Удалить Товар').add('Добавить Товар').add('Кол-во пользователей')




"""команда старт и ее выводы"""
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f"<b>{message.from_user.first_name}\nДобро пожаловать в магазин Кроссовок LUZZ_APP</b>",
                         parse_mode='HTML',
                         reply_markup=main)

    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы Зашли Как Администратор' , reply_markup=main_admin)





""""текст для ошибки"""
@dp.message_handler(text=['Связь'])
async def contacts(message: types.Message):
    await message.answer('Менеджер для покупки: @Hoperuu')


@dp.message_handler(text=['Админ-Панель'])
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ панель', reply_markup=admins_panel)

    else:
        await message.answer('Я Не Понимаю Тебя!')

@dp.message_handler(text=['Корзина'])
async def deletes(message: types.Message):
    await message.answer('Корзина Пуста')



@dp.message_handler(text=['Каталог'])
async def catalog(message: types.Message):
    await message.answer('бвбвбвбвбвбвбвбвбвбвбвбвб')

@dp.message_handler(text=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')




@dp.message_handler()
async def answer(message: types.Message):
    await message.answer('Я Не Понимаю Тебя!')


if __name__ == "__main__":
    executor.start_polling(dp)


