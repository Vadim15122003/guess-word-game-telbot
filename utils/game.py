class Game:
	chat_id: int
	participants = [int]

	def __init__(self, chat_id: int):
		self.chat_id = chat_id
		self.participants = []
	
	def add_participant(self, id: id):
		self.participants.append(id)

	def remove_participant(self, id: int):
		self.participants.remove(id)

	def get_participants(self):
		return self.participants
	