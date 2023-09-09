import telebot
from settings import token
import wikipedia

wikipedia.set_lang('ru')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'старт'])
def welcome(message):
    bot.send_message(message.chat.id, 'Саламчик, это ботик который пинает хуи')
@bot.message_handler(content_types=['text'])
def wiki(message):
    if message.text == 'хуй':
        bot.send_message('пидорас, сам соси себе хуй')
    else:
        low_r = message.text
        low_r = low_r.replace(" ", "_")
        page = wikipedia.page(low_r)
        bot.send_message(message.chat.id, page.summary)

bot.polling(none_stop=True)