# "Эхо-бот с таймером"
# Задача: Создать бота, который:
# Отвечает тем же сообщением, что прислал пользователь
# По команде /timer X ждет X секунд и пишет "Время вышло!"
# Имеет кнопку "Случайное число"
# Что нужно изучить:
# Базовые хендлеры сообщений
# Простые клавиатуры
# asyncio.sleep() для таймера

import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import random

TOKEN = "8612168994:AAHUdnZ39btUJ5IEriDMEES-l4-VhkwJMQI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


button = InlineKeyboardButton(text="Случайное число", callback_data="rand")
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Добро пожаловать в эхо бот!\n\nОн умеет:\n - Повторять сообщения;\n"
                         " - Отмерять время через команду /timer X\n - Генерировать случайное число",
                         reply_markup=keyboard)


@dp.message(Command('timer'))
async def timer(message: types.Message):
    parts = message.text.split()
    if len(parts) < 2 or not await is_int(parts[1]):
        await message.answer("Неверный формат!\nВводите /timer X\nгде X это кол-во секунд")
        return

    await asyncio.sleep(int(parts[1]))
    await message.answer("Время вышло!")


@dp.message(F.text)
async def echo_all(message: types.Message):
    await message.answer(message.text)


@dp.callback_query(F.data == "rand")
async def rand(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1,100000000000000000000)))


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
