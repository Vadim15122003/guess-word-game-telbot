from .game import Game

class Chat:
	language: str
	game: Game
	participants = set()

	def __init__(self):
		self.game = None
		self.language = 'en'

	def set_language(self, language: str):
		self.language = language

	def add_participant(self, id: int):
		self.participants.add(id)

	def in_game(self):
		return self.game != None

	def to_dict(self):
		return {
			'language': self.language,
			'game': self.game.to_dict() if self.game else None,
			'participants': list(self.participants)
		}

	@staticmethod
	def from_dict(data: dict):
		chat = Chat()
		chat.language = data['language']
		chat.game = Game.from_dict(data['game']) if data['game'] else None
		chat.participants = set(data['participants'])
		return chat
