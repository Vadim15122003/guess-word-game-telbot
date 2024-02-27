from telebot import TeleBot, apihelper
from dotenv import dotenv_values
from utils.decorators import group, exist, is_in_game, private_conv
from utils.chat import Chat
from telebot import types
from utils.language import get_translation
from utils.database import load_data, save_data
import json, random

# report_player
# report_word
# verify_my_word
# points
# reset_points (only by admins)

config = dotenv_values('.env')
bot = TeleBot(config['TELEGRAM_BOT_TOKEN'])
chats = {}

def is_group(message):
	chat_type = message.chat.type
	return True if chat_type == 'group' or chat_type == 'supergroup' else False

def private(first_name, user_id, chat_id, mesg_str):
	try:
		bot.send_message(user_id, mesg_str, parse_mode='HTML')
		return True
	except apihelper.ApiTelegramException as e:
		if e.error_code == 403 and chat_id in chats:
			bot.send_message(chat_id, f'{first_name} {get_translation("private_msg", chats[chat_id])}')
		return False
	
def get_user_chat(user_id):
	for chat_id, chat in chats.items():
		if chat.game and chat.game.exits_user(str(user_id)):
			return chat_id, chat
	return None, None

def next_action(game, chat, chat_id):
	if len(game.participants) < 3:
		bot.send_message(chat_id, get_translation('game_ended', chat))
		show_points(chat, chat_id)
		chat.game = None
	else:
		pers_nr, pers_id = list(game.numbers.items())[0]
		next_pers_nr, next_pers_id = list(game.numbers.items())[1]
		pers_name = game.participants[str(pers_id)]
		next_pers_name = game.participants[str(next_pers_id)]
		last_pers_nr, last_pers_id = list(game.numbers.items())[len(game.numbers) - 1]
		last_pers_name = game.participants[str(last_pers_id)]
		if game.asking:
			bot.send_message(chat_id, '(' + str(pers_nr) + ') ' + pers_name + get_translation('ask', chat)
							+ '(' + str(next_pers_nr) + ') ' + next_pers_name + get_translation('respond', chat))
		else:
			bot.send_message(chat_id, '(' + str(pers_nr) + ') ' + pers_name
							+ get_translation('responder', chat) + '(' + str(last_pers_nr) + ') ' + last_pers_name)
			
def show_points(chat, chat_id):
	msg = get_translation('points_info', chat)
	for player in chat.participants.values():
		msg += f'{player.first_name}: {player.points}\n'
	bot.send_message(chat_id, msg)

# public chats
@bot.message_handler(commands=['help'])
@exist(chats)
def help(message):
	if is_group(message):
		bot.send_message(message.chat.id, get_translation('help', chats[message.chat.id]))
	else:
		bot.send_message(message.chat.id, 'This command will show information about commands and bot usage')

@bot.message_handler(commands=['settings'])
@exist(chats)
@group(bot)
def settings(message):
	if not chats[message.chat.id].in_game():
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton(get_translation('ch_lang', chats[message.chat.id]), callback_data='change_lang'))
		bot.reply_to(message, get_translation('select_edit', chats[message.chat.id]), reply_markup=markup)
	else:
		bot.reply_to(message, get_translation('in_game', chats[message.chat.id]))

@bot.message_handler(commands=['start_game'])
@exist(chats)
@group(bot)
@is_in_game(chats, bot)
def start_game(message):
	chat = chats[message.chat.id]
	if not chat.in_game():
		if private(message.from_user.first_name, message.from_user.id, message.chat.id, get_translation('you_start', chat)):
			chat.start_game(message.from_user.id, message.from_user.first_name)
			save_data(chats)
			bot.send_message(message.chat.id, str(chat.game.get_participants_number()) + ' ' +
					  					message.from_user.first_name + ' ' + get_translation('joined', chat))
	else:
		bot.reply_to(message, get_translation('already_in_game', chat))
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(get_translation('join', chats[message.chat.id]), callback_data='join'))
	bot.send_message(message.chat.id, message.from_user.first_name + ' ' + get_translation('play', chat))
	bot.send_message(message.chat.id, get_translation('start_game', chat), reply_markup=markup)

@bot.message_handler(commands=['play'])
@exist(chats)
@group(bot)
def play(message):
	if not chats[message.chat.id].in_game():
		bot.reply_to(message, get_translation('not_in_game', chats[message.chat.id]))
	elif chats[message.chat.id].game.is_running():
		bot.reply_to(message, get_translation('game_running', chats[message.chat.id]))
	elif chats[message.chat.id].game.starter_id != message.from_user.id:
		bot.reply_to(message, chats[message.chat.id].game.starter_name + 
			   		get_translation('game_not_started_by_you', chats[message.chat.id]))
	elif chats[message.chat.id].game.get_participants_number() < 3:
		bot.reply_to(message, get_translation('not_enough_players', chats[message.chat.id]))
	else:
		try:
			with open('database/words.json', 'r') as file:
				words = json.load(file)[chats[message.chat.id].language]
				word = random.choice(words)
				del words
				chats[message.chat.id].game.play(word)
				save_data(chats)
				bot.send_message(message.chat.id, get_translation('game_started', chats[message.chat.id]))
				list_players: str = ''
				for nr, pers_id in chats[message.chat.id].game.numbers.items():
					list_players += str(nr) + '. ' + chats[message.chat.id].game.participants[str(pers_id)] + '\n'
				if list_players:
					bot.send_message(message.chat.id, list_players)
				bot.send_message(message.chat.id, get_translation('rules1', chats[message.chat.id])
					+ (str(len(chats[message.chat.id].game.person_to_guess)) + get_translation('rules3', chats[message.chat.id])
					if len(chats[message.chat.id].game.person_to_guess) > 1 else get_translation('rules2', chats[message.chat.id]))
					+ get_translation('rules4', chats[message.chat.id]))
				bot.send_message(message.chat.id, get_translation('rules5', chats[message.chat.id]))
				for nr, pers_id in chats[message.chat.id].game.numbers.items():
					if nr in chats[message.chat.id].game.person_to_guess:
						private(chats[message.chat.id].participants[str(pers_id)].first_name, pers_id, message.chat.id, 
							get_translation('you_guess', chats[message.chat.id]))
					else:
						private(chats[message.chat.id].participants[str(pers_id)].first_name, pers_id, message.chat.id, 
							get_translation('your_word', chats[message.chat.id]) + '<b>' + chats[message.chat.id].game.word + '</b>')
				asker_nr, asker_id = list(chats[message.chat.id].game.numbers.items())[0]
				answer_nr, answer_id = list(chats[message.chat.id].game.numbers.items())[1]
				asker_name = chats[message.chat.id].game.participants[str(asker_id)]
				answer_name = chats[message.chat.id].game.participants[str(answer_id)]
				bot.send_message(message.chat.id, '(' + str(asker_nr) + ') ' + asker_name + get_translation('ask', chats[message.chat.id])
									+ '(' + str(answer_nr) + ') ' + answer_name + get_translation('respond', chats[message.chat.id]))
		except FileNotFoundError:
			bot.send_message(message.chat.id, get_translation('no_words', chats[message.chat.id]))

# private chats
@bot.message_handler(commands=['report_player'])
@exist(chats)
@private_conv(bot, chats)
def report_player(message):
	_, chat = get_user_chat(message.from_user.id)
	if chat and chat.game.is_running():
		is_to_guess = False
		for pers_id in chat.game.person_to_guess.values():
			if pers_id == message.from_user.id:
				is_to_guess = True
				break
		if not is_to_guess:
			markup = types.InlineKeyboardMarkup()
			for i in range(1, len(chat.game.numbers) + 1):
				if chat.game.numbers[str(i)] != message.from_user.id:
					markup.add(types.InlineKeyboardButton('(' + str(i) + ') ' + chat.game.participants[str(chat.game.numbers[str(i)])],
											callback_data=f'report_{i}'))
			markup.add(types.InlineKeyboardButton('Anuleaza', callback_data='cancel_player_report'))
			bot.send_message(message.chat.id, 'Alegeti pe cine presupuneti ca nu stie cuvantul', reply_markup=markup)
	elif chat and chat.game.is_running():
		bot.send_message(message.chat.id, 'Tu esti persoana care nu stie cuvantul si trebuie sa ghicesti cuvantul, pentru aceasta tasteaza /report_word')
	elif chat:
		bot.send_message(message.chat.id, 'Inca nu a inceput jocul (cel ce a inceput jocul va trebui sa tasteze /play dupa ce toti participantii vor apasa sa participe)')
	else:
		bot.send_message(message.chat.id, 'Nu esti in niciun joc activ momentan')

@bot.message_handler()
@exist(chats)
def message_handle(message):
	if is_group(message):
		chat = chats[message.chat.id]
		if chat.in_game() and chat.game.is_running():
			game = chat.game
			pers_nr, pers_id = list(game.numbers.items())[0]
			next_pers_nr, next_pers_id = list(game.numbers.items())[1]
			pers_name = game.participants[str(pers_id)]
			next_pers_name = game.participants[str(next_pers_id)]
			last_pers_nr, last_pers_id = list(game.numbers.items())[len(game.numbers) - 1]
			last_pers_name = game.participants[str(last_pers_id)]
			if pers_id != message.from_user.id:
				msg_not_on_thme_allowed = 2
				if game.msg_not_on_theme > msg_not_on_thme_allowed - 1:
					game.msg_not_on_theme = 0
					if game.asking:
						bot.send_message(message.chat.id, '(' + str(pers_nr) + ') ' + pers_name + get_translation('ask', chat)
										+ '(' + str(next_pers_nr) + ') ' + next_pers_name + get_translation('respond', chat))
					else:
						bot.send_message(message.chat.id, '(' + str(pers_nr) + ') ' + pers_name
										+ get_translation('responder', chat) + '(' + str(last_pers_nr) + ') ' + last_pers_name)
				else:
					game.msg_not_on_theme += 1
			else:
				if game.asking:
					bot.send_message(message.chat.id, '(' + str(next_pers_nr) + ') ' + next_pers_name
										+ get_translation('responder', chat) + '(' + str(pers_nr) + ') ' + pers_name)
					del game.numbers[pers_nr]
					game.numbers[pers_nr] = pers_id
					game.asking = False
				else:
					bot.send_message(message.chat.id, '(' + str(pers_nr) + ') ' + pers_name + get_translation('ask', chat)
										+ '(' + str(next_pers_nr) + ') ' + next_pers_name + get_translation('respond', chats[message.chat.id]))
					game.asking = True
					game.reminder_cnt += 1
					reminder_cnt_allowed = 5
					if game.reminder_cnt >= reminder_cnt_allowed:
						bot.send_message(message.chat.id, get_translation('reminder', chat))
						game.reminder_cnt = 0
				game.msg_not_on_theme = 0
			save_data(chats)
	else:
		pass

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
	if not chats:
		chats.update(load_data())
	if call.message.chat.id not in chats and call.message.chat.type != 'private':
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
		user_id = call.from_user.id
		chat_id = call.message.chat.id
		for ch_id, chat in chats.items():
			if ch_id != chat_id and chat.game and chat.game.exits_user(str(user_id)):
				bot.send_message(ch_id, call.from_user.first_name + get_translation('is_in_game', chat))
				return
		if call.message.chat.id in chats and chats[call.message.chat.id].game and not chats[call.message.chat.id].game.is_running():
			chat = chats[call.message.chat.id]
			if chat.add_participant(call.from_user.id, call.from_user.first_name):
				if not private(call.from_user.first_name, call.from_user.id, call.message.chat.id, get_translation('you_join', chat)):
					chat.remove_participant(call.from_user.id)
				else:
					bot.send_message(call.message.chat.id, str(chat.game.get_participants_number()) + ' ' +
					  					call.from_user.first_name + ' ' + get_translation('joined', chat))
				save_data(chats)
			else:
				# bot.send_message(call.message.chat.id, call.from_user.first_name + ' deja participa')
				pass

	if call.data.startswith('report_'):
		chat_id, chat = get_user_chat(call.from_user.id)
		if chat and chat.game and chat.game.is_running():
			game = chat.game
			reported_nr = call.data.split('_')[1]
			reported_id = game.numbers[str(reported_nr)]
			reported_name = game.participants[str(reported_id)]
			reporter_name = call.from_user.first_name
			reporter_nr = game.get_nr_by_id(call.from_user.id)
			if reported_nr in game.numbers and str(reported_id) in game.participants:
				first_nr, _ = list(game.numbers.items())[0]
				last_nr, _ = list(game.numbers.items())[len(game.numbers) - 1]
				if last_nr == reported_nr or first_nr == reported_nr:
					game.asking = True
				if reported_nr in game.person_to_guess:
					game.remove_participant(reported_id)
					bot.send_message(call.message.chat.id, 'Ai ghicit corect, ' + reported_name + ' nu stia cuvantul, pentru aceasta primesti 2 puncte')
					bot.send_message(chat_id, '(' + str(reporter_nr) + ') ' + reporter_name + ' ' + get_translation("report_player", chat) +
					  				' (' + str(reported_nr) + ') ' + reported_name + ' ' + get_translation("report_succes", chat) + ' '
									+ str(len(game.person_to_guess)) + ' ' + get_translation("remained_to_guess", chat))
					bot.send_message(chat_id, '(' + str(reported_nr) + ') ' + reported_name + ' ' + get_translation("report_eliminated", chat) + 
					  				' (' + str(reporter_nr) + ') ' + reporter_name + ' ' + get_translation("report_get_points", chat))
					chat.add_points(call.from_user.id, 2)
					next_action(game, chat, chat_id)
				else:
					if last_nr == reporter_nr or first_nr == reporter_nr:
						game.asking = True
					game.remove_participant(reported_id)
					game.remove_participant(call.from_user.id)
					chat.add_points(call.from_user.id, -4)
					bot.send_message(call.message.chat.id, 'Nu ai ghicit, ' + reported_name + ' stia cuvantul, pentru aceasta ti se vor scadea 4 puncte')
					bot.send_message(chat_id, '(' + str(reporter_nr) + ') ' + reporter_name + ' ' + get_translation("report_player", chat)
					  				+ ' (' + str(reported_nr) + ') ' + reported_name + ' ' + get_translation("report_fail", chat) + ' 4 '
									+ get_translation("points", chat))
					bot.send_message(chat_id, get_translation('two_quit', chat))
					next_action(game, chat, chat_id)
				save_data(chats)
			else:
				bot.send_message(call.message.chat.id, f'({reported_nr}) {reported_name} nu mai este in acest joc')
		else:
			bot.send_message(call.message.chat.id, 'Nu esti in niciun joc activ momentan')
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

	if call.data == 'cancel_player_report':
		bot.send_message(call.message.chat.id, 'Operatie anulata')
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

bot.polling(non_stop=True)
