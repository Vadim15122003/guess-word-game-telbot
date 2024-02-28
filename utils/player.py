class Player:
	points: int = 0
	first_name: str
	word: str = None
	try_word: bool = False

	def __init__(self, first_name: str):
		self.first_name = first_name

	def add_points(self, points: int):
		self.points += points
	
	def to_dict(self):
		return {
			'points': self.points,
			'first_name': self.first_name,
			'word': self.word,
			'try_word': self.try_word
		}
	
	@staticmethod
	def from_dict(data: dict):
		player = Player(data['first_name'])
		player.points = data['points']
		player.word = data['word']
		player.try_word = data['try_word']
		return player
