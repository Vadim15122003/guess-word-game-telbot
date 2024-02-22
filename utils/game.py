class Game:
	participants = {}
	running = False
	starter_id: int
	starter_name: str

	def __init__(self):
		self.running = False
	
	def add_participant(self, id: id, first_name: str):
		if not id in self.participants:
			self.participants[id] = first_name
			return True
		return False

	def remove_participant(self, id: int):
		if id in self.participants:
			del self.participants[id]

	def get_participants(self):
		return self.participants
	
	def is_running(self):
		return self.running
	
	def start(self, starter: int, first_name: str):
		self.starter_id = starter
		self.starter_name = first_name
		self.participants[starter] = first_name

	def to_dict(self):
		return {
			'participants': self.participants,
			'running': self.running,
			'starter_id': self.starter_id,
			'starter_name': self.starter_name
		}
	
	@staticmethod
	def from_dict(data: dict):
		game = Game()
		game.participants = data['participants']
		game.running = data['running']
		game.starter_id = data['starter_id']
		game.starter_name = data['starter_name']
		return game
