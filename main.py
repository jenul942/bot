import os
import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1987421018:AAHfq6aNGFaWSGwDpNNBl1rNsXhRdLJHxRQ")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I will give you covid 19 states in sri lanka")


@bot.message_handler(commands=['deaths'])
def scrap(message):
  page = requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
  after_bs = BeautifulSoup(page.content, 'html.parser')
  find_data = after_bs.find_all(id="maincounter-number")
  output = ''
  for x in find_data:
    output = output + x.text
  bot.reply_to(message, output)

@bot.message_handler(commands=['cases'])
def scrap(message):
  page = requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
  after_bs = BeautifulSoup(page.content, 'html.parser')
  find_data = after_bs.find_all(id="maincounter-wrap")
  output = ''
  for x in find_data:
    output = output + x.text
  bot.reply_to(message, output)




bot.polling()
