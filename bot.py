import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import dotenv_values
from backend import get_random_aggressive_line, generate_random_ip

config = dotenv_values('.env')

bot = Bot(token=config["TOKEN"])
dp = Dispatcher()


@dp.message(F.text == 'Как дела?')
async def small_talk_message(message):
    await message.reply(f'Я знаю, где ты живешь: {generate_random_ip()}')

@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_aggressive_line())
    #await message.reply(generate_random_ip())
    

async def main():
    await dp.start_polling(bot)

asyncio.run(main())