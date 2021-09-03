import os
import telebot


bot = telebot.TeleBot("1987421018:AAHfq6aNGFaWSGwDpNNBl1rNsXhRdLJHxRQ")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm jenul Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "jenul")



bot.polling()