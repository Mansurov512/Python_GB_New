





from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler  # CallbackQueryHandler чтобы получать и узнавать какие-то события,
                                                                                                 # в нашем случае нажатие на кнопки
from credits import bot_token #файл с токеном бота

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

lines_file = []
day = {1: "Monday", 2: "Tuersday", 3: "Wendsday", 4: "Thursday", 5: "Friday"}
time = {1: "10:00-11:00", 2: "11:00-12:00", 3: "12:00-13:00", 4: "13:00-14:00"}

print("Бот запущен")

def start(update, context): # обработка сообщений пользователя
    print("Бот стартовал")
    context.bot.send_message(update.effective_chat.id, "Приветствуем в рабочем календаре на пол ставки!")
    keyboard = [
        [InlineKeyboardButton("Добавить новую задачу", callback_data='1')],
        [InlineKeyboardButton("Показать расписание дня недели", callback_data='2')],
        [InlineKeyboardButton("Удалить задачу", callback_data='3')]
    ]
    update.message.reply_text("Выберите что хотите сделать:", reply_markup=InlineKeyboardMarkup(keyboard))

def message1(update, context):
    # if update.message.text == "Боб": # последнее сообщение которое написал пользователь
    #     context.bot.send_message(update.effective_chat.id, "Привет!, Боб. Я ждал тебя!")
    # else:
    #     context.bot.send_message(update.effective_chat.id, "Ты не Боб. Уходи!(проверка работы отрицания) 26 декабря 2022 г")
    # line = update.message.text
    # print(line)

    #day_number = int(input("Введите номер дня недели от 1 до 5: "))
    context.bot.send_message(update.effective_chat.id, "Введите номер дня недели от 1 до 5: ")

    day_number = int(update.message.text)
    print(day_number)
    print(type(day_number))
    file_name = day[day_number] + ".txt"

    with open(file_name, "r", encoding="utf-8") as file:  # считываем содержимое файла в список
        lines_file = file.readlines()

    context.bot.register_next_step_handler(update.message.text, message2)

def message2(update, context):

    # day_time = int(input("Введите порядковый номер необходимого времени от 1 до 4, в котором:\n"
    #                      "1 - 10:00-11:00\n"
    #                      "2 - 11:00-12:00\n"
    #                      "3 - 12:00-13:00\n"
    #                      "4 - 13:00-14:00\n"))

    context.bot.send_message(update.effective_chat.id, "Введите порядковый номер необходимого времени от 1 до 4, в котором:")
                                                       # "1 - 10:00-11:00\n"
                                                       # "2 - 11:00-12:00\n"
                                                       # "3 - 12:00-13:00\n"
                                                       # "4 - 13:00-14:00\n")
    day_time = int(update.message.text)
    context.bot.register_next_step_handler(update.message.text, message3)

def message3(update, context):

    #task = input("Введите рабочую задачу для указанного времени: ")

    context.bot.send_message(update.effective_chat.id, "Введите рабочую задачу для указанного времени: ")
    task = update.message.text


# @bot.message_handler(content_types=['text'])
def button(update, context): #
    query = update.callback_query # update - все обновления,
    query.answer() # получаем все ответы
    if query.data == '1': # то что вводит пользователь
        #context.bot.send_message(update.effective_chat.id, "Введите номер дня недели от 1 до 5: ") # ответы пользователю
        message1(update, context)
        message2(update, context)
        message3(update, context)

        # #     if update.message.text == "Боб": # последнее сообщение которое написал пользователь
        # #         context.bot.send_message(update.effective_chat.id, "Привет!, Боб. Я ждал тебя!")
        # #day_number = update.getMessage()  # = int(input("Введите номер дня недели от 1 до 5: "))
        # global day_number
        # day_number = message.text  # = int(input("Введите номер дня недели от 1 до 5: "))
        # print(day_number.getText())
        # file_name = day[day_number] + ".txt"

        # with open(file_name, "r", encoding="utf-8") as file:  # считываем содержимое файла в список
        #     lines_file = file.readlines()


        context.bot.send_message(update.effective_chat.id, "*пока вроде работает раз видишь это сообщение*")

    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, "Вторник")
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, "Среда")



start_handler = CommandHandler('start', start) # задаём команду старт (через слэш - /start)
# commant_to_do_handler = CommandHandler('ctd', commant_to_do) # команда на получение клавиатуры с выбором дня недели
button_handler =  CallbackQueryHandler(button) # "от пользователя мы не ждём никаких действий, так как получаем их от сервера телеграмма"

dispatcher.add_handler(start_handler) # бот теперь знает что появилась та или иная команда
# dispatcher.add_handler(commant_to_do_handler)
dispatcher.add_handler(button_handler)

message_handler = MessageHandler(Filters.text, message1) # указываем какого типа у нас сообщения, в данном случае текст
# message2_handler = MessageHandler(Filters.text, message2) # указываем какого типа у нас сообщения, в данном случае текст
# message3_handler = MessageHandler(Filters.text, message3) # указываем какого типа у нас сообщения, в данном случае текст

dispatcher.add_handler(message_handler)
# dispatcher.add_handler(message2_handler)
# dispatcher.add_handler(message3_handler)


updater.start_polling()
updater.idle()

# def commant_to_do(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Добавить новую задачу", callback_data='1')],
#         [InlineKeyboardButton("Показать расписание дня недели", callback_data='2')],
#         [InlineKeyboardButton("Удалить задачу", callback_data='3')]
#     ]
#     update.message.reply_text("Выберите что хотите сделать:", reply_markup=InlineKeyboardMarkup(keyboard))


# def message(update, context):
#     if update.message.text == "Боб": # последнее сообщение которое написал пользователь
#         context.bot.send_message(update.effective_chat.id, "Привет!, Боб. Я ждал тебя!")
#     else:
#         context.bot.send_message(update.effective_chat.id, "Ты не Боб. Уходи!(проверка работы отрицания) 26 декабря 2022 г")
#
# def get_day(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Кнопка 1", callback_data='1'), InlineKeyboardButton("Вторник", callback_data='2')],
#         [InlineKeyboardButton("Среда", callback_data='3'), InlineKeyboardButton("Четверг", callback_data='4')],
#         [InlineKeyboardButton("Пятница", callback_data='5')]
#     ]
#     update.message.reply_text("Выбери день недели", reply_markup=InlineKeyboardMarkup(keyboard))
#
# def button(update, context): #
#     query = update.callback_query # update - все обновления,
#     query.answer() # получаем все ответы
#     if query.data == '1': # то что вводит пользователь
#         context.bot.send_message(update.effective_chat.id, "Понедельник!") # ответы пользователю
#     elif query.data == '2':
#         context.bot.send_message(update.effective_chat.id, "Вторник")
#     elif query.data == '3':
#             context.bot.send_message(update.effective_chat.id, "Среда")
#     elif query.data == '4':
#                 context.bot.send_message(update.effective_chat.id, "Четверг")
#     elif query.data == '5':
#                 context.bot.send_message(update.effective_chat.id, "Пятница")
#     # elif query.data == '6':
#     #             context.bot.send_message(update.effective_chat.id, "Суббота")
#


# getday_handler = CommandHandler('getday', get_day) # команда на получение клавиатуры с выбором дня недели
# # unknow_handler = MessageHandler(Filters.command, unknow) # можно сделать команду для обработки неизвестных команд
# message_handler = MessageHandler(Filters.text, message) # указываем какого типа у нас сообщения, в данном случае текст
#

# dispatcher.add_handler(getday_handler)
# dispatcher.add_handler(message_handler)








