from telebot import TeleBot, apihelper
from dotenv import dotenv_values

config = dotenv_values('.env')
bot = TeleBot(config['TELEGRAM_BOT_TOKEN'])

@bot.message_handler(commands=['private_msg'])
def private(message):
	try:
		user_id = message.from_user.id
		bot.send_message(user_id, "Mesaj privat")
	except apihelper.ApiTelegramException as e:
		if e.error_code == 403:
			user_name = message.from_user.first_name
			bot.reply_to(message, f'{user_name} te rog inițiază o conversație privată cu mine pentru ca sati pot trimite mesaje private')
     
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['status'])
def start(message):
    chat_member = bot.get_chat_member(message.chat.id, bot.get_me().id)
    if chat_member.status in ["administrator", "creator"]:
        bot.send_message(message.chat.id, "I'm an admin!")
    else:
        bot.send_message(message.chat.id, "I'm not an admin.")

bot.polling(non_stop=True)
