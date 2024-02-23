from .game import Game
from .player import Player
from typing import Dict

class Chat:
	language: str
	game: Game
	participants: Dict[int, Player] = {}

	def __init__(self):
		self.game = None
		self.language = 'en'

	def set_language(self, language: str):
		self.language = language

	def add_participant(self, id: int, first_name: str):
		if not id in self.participants:
			self.participants[id] = Player(first_name)
		return self.game.add_participant(id, first_name)
	
	def remove_participant(self, id: int):
		if id in self.participants:
			del self.participants[id]
		self.game.remove_participant(id)

	def in_game(self):
		return self.game != None
	
	def start_game(self, starter: int, first_name: str):
		self.game = Game()
		self.participants[starter] = Player(first_name)
		self.game.start(starter, first_name)
		return self.game

	def to_dict(self):
		return {
			'language': self.language,
			'game': self.game.to_dict() if self.game else None,
			'participants': {id: player.to_dict() for id, player in self.participants.items()}
		}

	@staticmethod
	def from_dict(data: dict):
		chat = Chat()
		chat.language = data['language']
		chat.game = Game.from_dict(data['game']) if data['game'] else None
		chat.participants = {id: Player.from_dict(player) for id, player in data['participants'].items()}
		return chat
