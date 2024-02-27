from .chat import Chat
from .database import load_data, save_data
from .language import get_translation

def group(bot, announce=True):
	def decorator(func):
		def wrapper(message):
			chat_type = message.chat.type
			if chat_type == 'group' or chat_type == 'supergroup':
				func(message)
			elif announce:
				bot.reply_to(message, 'Această comandă poate fi utilizată doar în grupuri, utilizați /help pentru detalii despre acest bot')
		return wrapper
	return decorator

def admin(chats, bot, announce=True):
	def decorator(func):
		def wrapper(message):
			chat_type = message.chat.type
			if chat_type == 'group' or chat_type == 'supergroup':
				chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
				if chat_member.status in ['member'] and announce:
					bot.reply_to(message, get_translation('admin', chats[message.chat.id]))
				else:
					func(message)
		return wrapper
	return decorator

def private_conv(bot, chats=None, announce=True):
	def decorator(func):
		def wrapper(message):
			chat_type = message.chat.type
			chat = chats[message.chat.id] if chats and message.chat.id in chats else None
			if chat_type == 'private':
				func(message)
			elif announce and chat:
				bot.reply_to(message, get_translation('private_conv', chat))
		return wrapper
	return decorator

def exist(chats):
	def decorator(func):
		def wrapper(message):
			if not chats:
				chats.update(load_data())
			if message.chat.id not in chats and message.chat.type != 'private':
				chats[message.chat.id] = Chat()
				save_data(chats)
			func(message)
		return wrapper
	return decorator

def is_in_game(chats, bot):
	def decorator(func):
		def wrapper(message):
			user_id = message.from_user.id
			chat_id = message.chat.id
			for ch_id, chat in chats.items():
				if ch_id != chat_id and chat.game and chat.game.exits_user(str(user_id)):
					bot.reply_to(message, message.from_user.first_name + get_translation('is_in_game', chat))
					return
			func(message)
		return wrapper
	return decorator
