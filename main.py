from telebot import TeleBot
from dotenv import dotenv_values

config = dotenv_values('.env')
bot = TeleBot(config['TELEGRAM_BOT_TOKEN'])

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, message)
	bot.send_message(message.chat.id, "hi")

bot.polling(non_stop=True)
