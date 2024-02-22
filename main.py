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

def private(first_name, user_id, chat_id, mesg_str):
	try:
		bot.send_message(user_id, mesg_str)
		return True
	except apihelper.ApiTelegramException as e:
		if e.error_code == 403 and chat_id in chats:
			bot.send_message(chat_id, f'{first_name} {get_translation("private_msg", chats[chat_id])}')
		return False

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
	else:
		bot.reply_to(message, get_translation('in_game', chats[message.chat.id]))

@bot.message_handler(commands=['start_game'])
@group(bot)
@exist(chats)
def start_game(message):
	chat = chats[message.chat.id]
	if not chat.in_game():
		if private(message.from_user.first_name, message.from_user.id, message.chat.id, get_translation('you_start', chat)):
			chat.start_game(message.from_user.id, message.from_user.first_name)
			save_data(chats)
	else:
		bot.reply_to(message, get_translation('already_in_game', chat))
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(get_translation('join', chats[message.chat.id]), callback_data='join'))
	bot.send_message(message.chat.id, message.from_user.first_name + ' ' + get_translation('play', chat))
	bot.send_message(message.chat.id, get_translation('start_game', chat), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
	if not chats:
		chats.update(load_data())
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

	if call.data == 'join':
		if not chats:
			chats.update(load_data())
		if call.message.chat.id in chats and chats[call.message.chat.id].game and not chats[call.message.chat.id].game.is_running():
			chat = chats[call.message.chat.id]
			if chat.add_participant(call.from_user.id, call.from_user.first_name):
				if not private(call.from_user.first_name, call.from_user.id, call.message.chat.id, get_translation('you_join', chat)):
					chat.remove_participant(call.from_user.id)
				else:
					bot.send_message(call.message.chat.id, call.from_user.first_name + ' ' + get_translation('joined', chat))
				save_data(chats)
			else:
				# bot.send_message(call.message.chat.id, call.from_user.first_name + ' deja participa')
				pass

bot.polling(non_stop=True)
