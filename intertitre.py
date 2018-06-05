import configparser
import telebot
from telebot import types
import browse

##import time
##from time import sleep
##from collections import namedtuple
##import Edit_sheet
##import httplib2
##import argparse
##from apiclient import discovery
##from oauth2client import client
##from oauth2client import tools
##from oauth2client.file import Storage

config = configparser.ConfigParser()
config.read('config.ini')
bot = telebot.TeleBot(config['DEFAULT']['Token'])

commands = {  'start': 'Описание бота',
              'help': 'Список команд'
           }

@bot.message_handler(commands=['start'])
def start(m):
    cid = m.chat.id
    bot.send_message(cid, 'Привет, этот бот подгружает случайный титр с сайта http://intertitre.togdazine.ru/')

@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    help_text = 'Доступны команды: \n'
    for key in commands:  
        help_text += '/' + key + ': '
        help_text += commands[key] + '\n'
    bot.send_message(cid, help_text)  

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def titre(query):
    qid = query.id
    f = browse.get()
    p = []
    for i,j in enumerate(f):
      p.append(types.InlineQueryResultPhoto(id = 'i', photo_url = j, thumb_url = j))
    bot.answer_inline_query(qid, p, cache_time = 1)
   

if __name__ == '__main__':
    bot.polling(none_stop=True) 


