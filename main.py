import telebot
import os
import config
import hackpy

bot = telebot.TeleBot(config.TOKEN)
admin_id = config.ADMIN_ID

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("/manager_process", "/desktop_video", "/screenshot_desktop")
keyboard1.row("/camera", "/microphone")#Control Environment
keyboard1.row("/restart", "/sleep_mode")#control machine

def auth(func):
    def wrapper(message):
        if str(message.chat.id) != admin_id:
            bot.send_message(message.chat.id, "Это не твой бот! Иди нафиг!)")
            return
        else:
            func(message)
    return wrapper

@bot.message_handler(commands=['start'])
@auth
def start(message):
    bot.send_message(message.chat.id, "Start bot", reply_markup=keyboard1)

@bot.message_handler(commands=["manager_process", "desktop_video", "screenshot_desktop"])
@auth
def controlProcess(message):
    if message.text == '/manager_process':
        bot.send_message(message.chat.id, "manager_process")
    elif message.text == '/desktop_video':
        bot.send_message(message.chat.id, "desktop_video")
    elif message.text == '/screenshot_desktop':
        bot.send_message(message.chat.id, "screenshot_desktop")

@bot.message_handler(commands=["camera", "microphone"])
@auth
def controlEnvironment(message):
    pass

@bot.message_handler(commands=["restart", "sleep_mode"])
@auth
def controlMachine(message):
    pass

bot.polling()
