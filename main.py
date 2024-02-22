from telebot import TeleBot, apihelper
from dotenv import dotenv_values
from utils.decorators import group, exist
from utils.chat import Chat
from telebot import types
from utils.language import get_translation
from utils.database import load_data, save_data
import json

config = dotenv_values('.env')
bot = TeleBot(config['TELEGRAM_BOT_TOKEN'])
chats = {}

def is_group(message):
	chat_type = message.chat.type
	return True if chat_type == 'group' or chat_type == 'supergroup' else False

@bot.message_handler(commands=['help'])
def help(message):
	if not chats:
		chats.update(load_data())
	if is_group(message):
		if message.chat.id not in chats:
			chats[message.chat.id] = Chat()
			save_data(chats)
		bot.send_message(message.chat.id, get_translation('help', chats[message.chat.id]))
	else:
		bot.send_message(message.chat.id, 'This command will show information about commands and bot usage')

@bot.message_handler(commands=['settings'])
@group(bot)
@exist(chats)
def settings(message):
	if not chats[message.chat.id].in_game():
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton(get_translation('ch_lang', chats[message.chat.id]), callback_data='change_lang'))
		bot.reply_to(message, get_translation('select_edit', chats[message.chat.id]), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
	if call.message.chat.id not in chats:
		chats[call.message.chat.id] = Chat()
	if call.data == 'change_lang' and not chats[call.message.chat.id].in_game():
		try:
			with open('database/languages.json', 'r') as file:
				languages = json.load(file)['languages']
		except FileNotFoundError:
			languages = []
		
		markup = types.InlineKeyboardMarkup()
		buttons = [types.InlineKeyboardButton(language, callback_data=f'language_{language}') for language in languages]
		for i in range(0, len(buttons), 3):
			markup.add(*buttons[i:i+3])		
		markup.add(types.InlineKeyboardButton(get_translation('cancel', chats[call.message.chat.id]), callback_data='language_cancel'))
		bot.send_message(call.message.chat.id, get_translation('select_lang', chats[call.message.chat.id]), reply_markup=markup)
		# to remove button after clickin on it
		# bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
	if call.data.startswith('language') and not chats[call.message.chat.id].in_game():
		lang = call.data.split('_')[1]
		if lang == 'cancel':
			bot.send_message(call.message.chat.id, get_translation('op_cancel', chats[call.message.chat.id]))
		else:
			chats[call.message.chat.id].set_language(lang)
			save_data(chats)
			bot.send_message(call.message.chat.id, get_translation('op_lang_success', chats[call.message.chat.id]))
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

# @bot.message_handler(commands=['private_msg'])
# def private(message):
# 	try:
# 		user_id = message.from_user.id
# 		bot.send_message(user_id, "Mesaj privat")
# 	except apihelper.ApiTelegramException as e:
# 		if e.error_code == 403:
# 			user_name = message.from_user.first_name
# 			bot.reply_to(message, f'{user_name} te rog inițiază o conversație privată cu mine pentru ca sati pot trimite mesaje private')
     
# @bot.message_handler(commands=['start'])
# def start(message):
# 	bot.send_message(message.chat.id, message)

# @bot.message_handler(commands=['status'])
# def start(message):
#     chat_member = bot.get_chat_member(message.chat.id, bot.get_me().id)
#     if chat_member.status in ["administrator", "creator"]:
#         bot.send_message(message.chat.id, "I'm an admin!")
#     else:
#         bot.send_message(message.chat.id, "I'm not an admin.")

bot.polling(non_stop=True)
