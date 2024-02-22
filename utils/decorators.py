from .chat import Chat
from .database import load_data, save_data

def group(bot):
	def decorator(func):
		def wrapper(message):
			chat_type = message.chat.type
			if chat_type == 'group' or chat_type == 'supergroup':
				func(message)
			else:
				bot.reply_to(message, 'This command can only be used in groups, use /help for details about this bot')
		return wrapper
	return decorator

def exist(chats):
	def decorator(func):
		def wrapper(message):
			if not chats:
				chats.update(load_data())
			if message.chat.id not in chats:
				chats[message.chat.id] = Chat()
				save_data(chats)
			func(message)
		return wrapper
	return decorator
