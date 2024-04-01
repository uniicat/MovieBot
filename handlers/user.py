import datetime

import telebot.types
from telebot.handler_backends import StatesGroup, State

from init_bot import bot


class User(StatesGroup):
    name = State()


def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0 <= current_time.hour < 6:
        return 'Доброй ночи'
    if 6 <= current_time.hour < 12:
        return 'Доброе утречко'
    if 12 <= current_time.hour < 18:
        return 'Добрый денёчек'
    else:
        return 'Добрый вечерок'


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    bot.set_state(message.from_user.id, User.name, message.chat.id)
    bot.send_message(message.chat.id, f'{get_welcome()}! Я бот для выбора фильма на вечер <3\nКак тебя зовут?')


@bot.message_handler(state=User.name)
def name(message: telebot.types.Message):
    with bot.retrieve_data(message.from_user.id) as data:
        data['name'] = message.text
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, f'Приятно познакомиться, {data['name']}!')
    bot.send_message(message.chat.id, 'Для того, чтобы подобрать фильм, отправьте: /get_movie')
