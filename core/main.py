import telebot
from telebot import types
import os
import random

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

keyboard = types.ReplyKeyboardMarkup(
    row_width=2, resize_keyboard=True, one_time_keyboard=True
)
button1 = types.KeyboardButton("ارتباط مستقیم با ما")
button2 = types.KeyboardButton("ثبت مشکل")
keyboard.add(button1, button2)


@bot.message_handler(commands=["start"])
def send_message(message):
    bot.reply_to(message, "از دکمه های زیر استفاده کنید :", reply_markup=keyboard)


def save_problem(message):
    problem = message.text
    ticket_number = random.randint(10000, 99999)
    bot.send_message(
        message.chat.id,
        f"کارشناسان ما در اسرع وقت با شما تماس خواهند گرفت . شماره پیگیری تیکت {ticket_number} می باشد.",
    )


@bot.message_handler(func=lambda message: message.text == "ثبت مشکل")
def erport_problem(message):
    bot.send_message(message.chat.id, "لطفا مشکل خود را وارد نمایید.")
    bot.register_next_step_handler(message, save_problem)


@bot.message_handler(func=lambda message: message.text == "ارتباط مستقیم با ما")
def contact_us(message):
    text = """
    برای ارتباط مستقیم با ما میتوانید با شماره های پشتیبانی که در زیر آمده است تماس حاصل فرمایید:
0912*******
021********
    """
    bot.send_message(message.chat.id, text)


bot.infinity_polling()
