import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('Здесь впиши токен, полученный от @botfather')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)

# import telebot;
# bot = telebot.TeleBot('5940435235:AAF38YAIl2N4LDzQ3cnsJKDLH3MO9L96EDs');
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
# from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
# from credits import bot_token #файл с токеном бота
#
# # bot = Bot(bot_token)
# updater = Updater(bot_token, use_context=True)
# dispatcher = updater.dispatcher
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#
# bot.polling(none_stop=True, interval=0)