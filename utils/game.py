import random

class Game:
	participants = {}
	running = False
	starter_id: int
	starter_name: str
	word: str = None
	numbers = {}
	person_to_guess = {}
	msg_not_on_theme = 0
	asking = True

	def __init__(self):
		self.running = False
	
	def add_participant(self, id: int, first_name: str):
		if not id in self.participants:
			self.participants[id] = first_name
			self.numbers[len(self.numbers) + 1] = id
			return True
		return False

	def remove_participant(self, id: int):
		if id in self.participants:
			del self.participants[id]

	def get_participants_number(self):
		return len(self.participants)
	
	def is_running(self):
		return self.running
	
	def start(self, starter: int, first_name: str):
		self.starter_id = starter
		self.starter_name = first_name
		self.add_participant(starter, first_name)

	def play(self, word: str):
		self.running = True
		self.word = word
		self.asking = True
		nr_to_guess = self.get_participants_number() // 10 + 1
		if self.numbers:
			while nr_to_guess > 0:
				person_nr, person_id = random.choice(list(self.numbers.items()))
				if not person_nr in self.person_to_guess:
					self.person_to_guess[person_nr] = person_id
					nr_to_guess -= 1

	def to_dict(self):
		return {
			'participants': self.participants,
			'running': self.running,
			'starter_id': self.starter_id,
			'starter_name': self.starter_name,
			'word': self.word if self.word else None,
			'numbers': self.numbers,
			'person_to_guess': self.person_to_guess,
			'msg_not_on_theme': self.msg_not_on_theme,
			'asking': self.asking
		}
	
	@staticmethod
	def from_dict(data: dict):
		game = Game()
		game.participants = data['participants']
		game.running = data['running']
		game.starter_id = data['starter_id']
		game.starter_name = data['starter_name']
		game.word = data['word']
		game.numbers = data['numbers']
		game.person_to_guess = data['person_to_guess']
		game.msg_not_on_theme = data['msg_not_on_theme']
		game.asking = data['asking']
		return game
