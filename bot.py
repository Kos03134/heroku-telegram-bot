# -*- coding: utf-8 -*-
import redis
# import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
# token = os.environ['TELEGRAM_TOKEN']
# some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
# r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot('968928190:AAE8iCHSU63HAcommSlsoVg_5J0OP2gNfw8')
# some_api = some_api_lib.connect(968928190:AAE8iCHSU63HAcommSlsoVg_5J0OP2gNfw8)
#              ...

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'you`ve entered command /start')



@bot.message_handler(content_types=['text'])
def send_text(message):
    if ' ' in message.text:
        bot.reply_to(message, "Здравствуй, {0.first_name}".format(message.from_user))
       # bot.send_message(message.chat.id, 'Viva 2JC')
    elif message.text != "":
        bot.send_message(message.chat.id, 'Привіт, {0.first_name}'.format(message.from_user))
bot.polling()
