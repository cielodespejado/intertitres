import configparser
import telebot
from telebot import types
import browse

config = configparser.ConfigParser()
config.read('config.ini')
bot = telebot.TeleBot(config['DEFAULT']['Token'])

commands = {  'start': 'Описание бота',
              'help': 'Список команд'
           }

@bot.message_handler(commands=['start'])
def start(m):
    cid = m.chat.id
    bot.send_message(cid, 'Привет, этот бот подгружает случайный титр с сайта http://intertitre.togdazine.ru/.')

@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    bot.send_message(cid, 'Как это работает: после вызова бота введите любой символ в поле сообщения.')  

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def titre(query):
    qid = query.id
    f = browse.get()
    p = []
    for i,j in enumerate(f):
      p.append(types.InlineQueryResultPhoto(id = i, photo_url = j, thumb_url = j, photo_width = 625, photo_height = 469))
    bot.answer_inline_query(qid, p, cache_time = 1)
   

if __name__ == '__main__':
    bot.polling(none_stop=True) 


