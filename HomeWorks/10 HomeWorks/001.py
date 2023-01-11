# Создать телеграм бота, поместить в него парсер и \ или ежедневник из последних ДЗ.

from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler  # CallbackQueryHandler чтобы получать и узнавать какие-то события,
                                                                                                 # в нашем случае нажатие на кнопки
from credits import bot_token #файл с токеном бота

import requests
from bs4 import BeautifulSoup as bs

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

print("Программа бота запущена")

def start(update, context): # обработка сообщений пользователя

    print("Бот стартовал")

    keyboard = [
        [InlineKeyboardButton("Узнать температуру в Санкт-Петербурге", callback_data='1')],
        [InlineKeyboardButton("Узнать курс доллара ЦБ", callback_data='2')]
    ]
    update.message.reply_text("Приветствуем Вас! Выберите действие:", reply_markup=InlineKeyboardMarkup(keyboard))

def date(update, context): # дата и время Мск
    url = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'
    response = requests.get(url).text
    # print(response)
    soup = bs(response, "html.parser")
    date_today = soup.find('div', "information__header__left__date")  # парсим сегодняшний день с датой и временем
    context.bot.send_message(update.effective_chat.id, date_today.text.strip())

def button_choiсe(update, context): #
    query = update.callback_query # update - все обновления,
    query.answer() # получаем все ответы
    if query.data == '1': # то что вводит пользователь
        url = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'
        response = requests.get(url).text
        # print(response)
        soup = bs(response, "html.parser")
        temperature = soup.find('div', "information__content__temperature")  # парсим температуру
        date_today = soup.find('div', "information__header__left__date")  # парсим сегодняшний день с датой и временем

        context.bot.send_message(update.effective_chat.id, "Температура на улице " + temperature.text.strip())

    elif query.data == '2':
        url = 'https://www.banki.ru/products/currency/cash/usd/sankt-peterburg/'  # https://beta.gismeteo.ru
        response = requests.get(url).text
        # print(response)
        soup = bs(response, "html.parser")
        exchange = soup.find('div', "currency-table__large-text")  # курс валюты

        context.bot.send_message(update.effective_chat.id, "Курс ЦБ " + exchange.text + " рубля за 1 доллар США.")

button_choiсe_handler =  CallbackQueryHandler(button_choiсe) # "от пользователя мы не ждём никаких действий, так как получаем их от сервера телеграмма"
start_handler = CommandHandler('start', start) # задаём команду старт (через слэш - /start)
date_handler = CommandHandler('date', date) # задаём команду старт (через слэш - /start)

dispatcher.add_handler(start_handler) # бот теперь знает что появилась та или иная команда
dispatcher.add_handler(date_handler)
dispatcher.add_handler(button_choiсe_handler)

updater.start_polling()
updater.idle()


# def keyboard_city(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Санкт-Петербург", callback_data='3')]
#     ]
#     # update.message.reply_text("Приветствуем Вас! Выберите что хотите сделать:",
#     #                           reply_markup=InlineKeyboardMarkup(keyboard))

# def button_city(update, context):
#     query = update.callback_query # update - все обновления,
#     query.answer() # получаем все ответы
#     if query.data == '3': # то что вводит пользователь
#         context.bot.send_message(update.effective_chat.id, "Понедельник!") # ответы пользователю