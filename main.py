import asyncio
import logging
import sys
from os import getenv

from openai import OpenAI
import requests
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "5346235377:AAGg1mWc4FPRxGn1GFcnOBcj75MMLlrAJlA"
OPENAI_API_KEY = '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'
DJANGO_API_URL = 'https://melsov.ru/product-list-api/'

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет! Я бот для консультации по сборке компьютеров. Задай мне вопрос!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        user_message = message.text

        # Получение данных из базы данных Django
        response = requests.get(DJANGO_API_URL)
        products = response.json()
        client = OpenAI(api_key=OPENAI_API_KEY)

        # Формирование запроса к GPT-4
        prompt = f'Пользователь: {user_message}\nСписок товаров: {products}\nОтвет:'

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that helps with computer part selection."},
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message)
        answer = response.choices[0].message.content

        await message.reply(answer, parse_mode=ParseMode.MARKDOWN)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())