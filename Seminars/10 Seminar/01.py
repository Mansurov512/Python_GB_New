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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits import bot_token

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!")

def message(update, context):
    if update.message.text == "Боб":
        context.bot.send_message(update.effective_chat.id, "Привет!, Боб. Я ждал тебя!")
    else:
        context.bot.send_message(update.effective_chat.id, "Ты не Боб. Уходи!")

def get_day(update, context):
    keyboard = [
        [InlineKeyboardButton("Понедельник", callback_data='1'), InlineKeyboardButton("Вторник", callback_data='2')],
        [InlineKeyboardButton("Среда", callback_data='3'), InlineKeyboardButton("Четверг", callback_data='4')]
    ]
    update.message.reply_text("Выбери день недели", reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    query =update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id, "Понедельник!")
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, "Вторник")
    elif query.data == '3':
            context.bot.send_message(update.effective_chat.id, "Среда")
    elif query.data == '4':
                context.bot.send_message(update.effective_chat.id, "Четверг")

button_handler =  CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
getday_handler = CommandHandler('getday', get_day)
# unknow_handler = MessageHandler(Filters.command, unknow)
message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getday_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()






