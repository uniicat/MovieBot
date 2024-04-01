import random

import telebot.types

from init_bot import bot



@bot.message_handler(commands=['get_movie'])
def genre(message: telebot.types.Message):
    text = 'Какой жанр посмотрим? :^'
    markup = telebot.util.quick_markup({
        'Комедия': {'callback_data': 'comedy'},
        'Фантастика': {'callback_data': 'science-fiction'},
        'Приключения': {'callback_data': 'adventure'},
        'Мультфильмы': {'callback_data': 'animation'},
        'Боевики': {'callback_data': 'action'},
    })
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'comedy')
def comedy_choose(callback: telebot.types.CallbackQuery):
    with open('genres/comedy.txt', 'r', encoding='utf-8') as file:
        comedies = file.read().split('\n')
    movie = random.choice(comedies)
    bot.send_message(callback.message.chat.id, f'Сегодня вечером стоит посмотреть - {movie}')


@bot.callback_query_handler(func=lambda callback: callback.data == 'science-fiction')
def science_fiction_choose(callback: telebot.types.CallbackQuery):
    with open('genres/science_fiction.txt', 'r', encoding='utf-8') as file:
        scifi = file.read().split('\n')
    movie = random.choice(scifi)
    bot.send_message(callback.message.chat.id, f'Сегодня вечером стоит посмотреть - {movie}')


@bot.callback_query_handler(func=lambda callback: callback.data == 'adventure')
def adventure_choose(callback: telebot.types.CallbackQuery):
    with open('genres/adventure.txt', 'r', encoding='utf-8') as file:
        adventures = file.read().split('\n')
    movie = random.choice(adventures)
    bot.send_message(callback.message.chat.id, f'Сегодня вечером стоит посмотреть - {movie}')


@bot.callback_query_handler(func=lambda callback: callback.data == 'animation')
def animation_choose(callback: telebot.types.CallbackQuery):
    with open('genres/animation.txt', 'r', encoding='utf-8') as file:
        animations = file.read().split('\n')
    movie = random.choice(animations)
    bot.send_message(callback.message.chat.id, f'Сегодня вечером стоит посмотреть - {movie}')


@bot.callback_query_handler(func=lambda callback: callback.data == 'action')
def action_choose(callback: telebot.types.CallbackQuery):
    with open('genres/action.txt', 'r', encoding='utf-8') as file:
        actions = file.read().split('\n')
    movie = random.choice(actions)
    bot.send_message(callback.message.chat.id, f'Сегодня вечером стоит посмотреть - {movie}')



