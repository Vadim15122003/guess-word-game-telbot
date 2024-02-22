class Player:
	points: int = 0
	first_name: str

	def __init__(self, first_name: str):
		self.first_name = first_name

	def add_points(self, points: int):
		self.points += points
	
	def to_dict(self):
		return {
			'points': self.points,
			'first_name': self.first_name
		}
	
	@staticmethod
	def from_dict(data: dict):
		player = Player(data['first_name'])
		player.points = data['points']
		return player
