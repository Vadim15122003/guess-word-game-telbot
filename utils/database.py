import json
from typing import Dict
from utils.chat import Chat

def save_data(chats: Dict[int, Chat]):
	with open('database/chats.json', 'w') as file:
		chats_dict = {k: v.to_dict() for k, v in chats.items()}
		json.dump(chats_dict, file, indent=4)

def load_data() -> Dict[int, Chat]:
	try:
		with open('database/chats.json', 'r') as file:
			chats_dict = json.load(file)
	except FileNotFoundError and json.JSONDecodeError:
		chats_dict = {}
	chats = {int(k): Chat.from_dict(v) for k, v in chats_dict.items()}
	return chats
