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
	reminder_cnt = 0
	asking = True

	def __init__(self):
		self.running = False
	
	def add_participant(self, id, first_name: str):
		if not str(id) in self.participants:
			self.participants[str(id)] = first_name
			self.numbers[len(self.numbers) + 1] = id
			return True
		return False
	
	def exits_user(self, id):
		return str(id) in self.participants

	def remove_participant(self, id):
		if str(id) in self.participants:
			del self.participants[str(id)]
		for nr, person_id in self.numbers.items():
			if int(person_id) == int(id):
				del self.numbers[nr]
				if nr in self.person_to_guess:
					del self.person_to_guess[nr]
				break

	def get_participants_number(self):
		return len(self.participants)
	
	def get_nr_by_id(self, id: int):
		for nr, person_id in self.numbers.items():
			if person_id == id:
				return nr
		return None
	
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
			'reminder_cnt': self.reminder_cnt,
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
		game.reminder_cnt = data['reminder_cnt'] if 'reminder_cnt' in data else 0
		game.asking = data['asking']
		return game
