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
