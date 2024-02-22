class Game:
	participants = [int]

	def __init__(self):
		self.participants = []
	
	def add_participant(self, id: id):
		if id not in self.participants:
			self.participants.append(id)

	def remove_participant(self, id: int):
		self.participants.remove(id)

	def get_participants(self):
		return self.participants

	def to_dict(self):
		return {
			'participants': self.participants
		}
	
	@staticmethod
	def from_dict(data: dict):
		game = Game()
		game.participants = data['participants']
		return game
