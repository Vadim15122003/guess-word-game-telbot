from .game import Game
from .player import Player
from typing import Dict

class Chat:
	language: str
	game: Game
	participants: Dict[int, Player] = {}
	last_game_word: str = None
	last_game_participants:int = None

	def __init__(self):
		self.game = None
		self.language = 'en'

	def set_language(self, language: str):
		self.language = language

	def add_participant(self, id, first_name: str):
		if not str(id) in self.participants:
			self.participants[str(id)] = Player(first_name)
		return self.game.add_participant(id, first_name)
	
	def remove_participant(self, id: int):
		if id in self.participants:
			del self.participants[id]
		self.game.remove_participant(id)

	def in_game(self):
		return self.game != None
	
	def start_game(self, starter: int, first_name: str):
		self.game = Game()
		self.add_participant(starter, first_name)
		self.game.start(starter, first_name)
		self.last_game_word = None
		self.last_game_participants = None
		for player in self.participants.values():
			player.word = None
			player.try_word = False
		return self.game
	
	def add_points(self, id, points: int):
		self.participants[str(id)].add_points(points)

	def to_dict(self):
		return {
			'language': self.language,
			'game': self.game.to_dict() if self.game else None,
			'participants': {id: player.to_dict() for id, player in self.participants.items()},
			'last_game_word': self.last_game_word,
			'last_game_participants': self.last_game_participants
		}

	@staticmethod
	def from_dict(data: dict):
		chat = Chat()
		chat.language = data['language']
		chat.game = Game.from_dict(data['game']) if data['game'] else None
		chat.participants = {id: Player.from_dict(player) for id, player in data['participants'].items()}
		chat.last_game_word = data['last_game_word']
		chat.last_game_participants = data['last_game_participants']
		return chat
