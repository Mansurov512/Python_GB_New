# https://telegram.org/dl/desktop/win
#
# BotFather
#
# /newbot
#
# qwertyMMR_bot
#
# 5940435235:AAF38YAIl2N4LDzQ3cnsJKDLH3MO9L96EDs
# pip install python-telegram-bot
# pip install telegram
# pip uninstall telegram
# pip uninstall python-telegram-bot
# C:\Users\Mikhail\Desktop\GB New\003 Python\Python_GB_New\Python_GB_New\lib\site-packages\telegram
# pip3 install --upgrade --force-reinstall python_telegram_bot
# pip install pyTelegramBotApi
# python.exe -m pip install --upgrade pip

from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler # CallbackQueryHandler чтобы получать и узнавать какие-то события,
                                                                                                # в нашем случае нажатие на кнопки
from credits import bot_token #файл с токеном бота

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context): # обработка сообщений пользователя
    context.bot.send_message(update.effective_chat.id, "Привет!")

def message(update, context):
    if update.message.text == "Боб": # последнее сообщение которое написал пользователь
        context.bot.send_message(update.effective_chat.id, "Привет!, Боб. Я ждал тебя!")
    else:
        context.bot.send_message(update.effective_chat.id, "Ты не Боб. Уходи!(проверка работы отрицания) 26 декабря 2022 г")

def get_day(update, context):
    keyboard = [
        [InlineKeyboardButton("Понедельник", callback_data='1'), InlineKeyboardButton("Вторник", callback_data='2')],
        [InlineKeyboardButton("Среда", callback_data='3'), InlineKeyboardButton("Четверг", callback_data='4')],
        [InlineKeyboardButton("Пятница", callback_data='5')]
    ]
    update.message.reply_text("Выбери день недели", reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context): #
    query = update.callback_query # update - все обновления,
    query.answer() # получаем все ответы
    if query.data == '1': # то что вводит пользователь
        context.bot.send_message(update.effective_chat.id, "Понедельник!") # ответы пользователю
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, "Вторник")
    elif query.data == '3':
            context.bot.send_message(update.effective_chat.id, "Среда")
    elif query.data == '4':
                context.bot.send_message(update.effective_chat.id, "Четверг")
    elif query.data == '5':
                context.bot.send_message(update.effective_chat.id, "Пятница")
    # elif query.data == '6':
    #             context.bot.send_message(update.effective_chat.id, "Суббота")

button_handler =  CallbackQueryHandler(button) # "от пользователя мы не ждём никаких действий, так как получаем их от сервера телеграмма"
start_handler = CommandHandler('start', start) # задаём команду старт (через слэш - /start)
getday_handler = CommandHandler('getday', get_day) # команда на получение клавиатуры с выбором дня недели
# unknow_handler = MessageHandler(Filters.command, unknow) # можно сделать команду для обработки неизвестных команд
message_handler = MessageHandler(Filters.text, message) # указываем какого типа у нас сообщения, в данном случае текст

dispatcher.add_handler(start_handler) # бот теперь знает что появилась та или иная команда
dispatcher.add_handler(getday_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()






