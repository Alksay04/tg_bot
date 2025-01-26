import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from dotenv import dotenv_values
from backend import get_random_aggressive_line, generate_random_ip
from users.users import create_user, read_users

config = dotenv_values('.env')

bot = Bot(token=config["TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def start_cmd(message):
    user_id = message.from_user.id
    config = {
        'ip': generate_random_ip(),
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
        'language_code': message.from_user.language_code,
        'is_premium': message.from_user.is_premium
    }


    create_user(user_id = user_id, config=config)
    first_name = config['first_name']
    await message.reply(f'Привет, {first_name}:\nЯ уже записал все твои данные.')

@dp.message(F.text == 'Как дела?')
async def small_talk_message(message):
    user_id = message.from_user.id
    ip = read_users(user_id=user_id)['id']
    await message.reply(f'Я знаю, где ты живешь: {ip}')

@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_aggressive_line())
    #await message.reply(generate_random_ip())
    

async def main():
    await dp.start_polling(bot)

asyncio.run(main())