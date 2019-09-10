# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
 bot = telebot.TeleBot(968928190:AAE8iCHSU63HAcommSlsoVg_5J0OP2gNfw8)
 #some_api = some_api_lib.connect(968928190:AAE8iCHSU63HAcommSlsoVg_5J0OP2gNfw8)
#              ...
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
