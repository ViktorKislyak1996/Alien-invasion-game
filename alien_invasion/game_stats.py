

class GameStats():
	# Отслеживание статисткики для игры Alien Invasion

	def __init__(self, ai_settings):
		# Инициализирует статистику
		self.ai_settings = ai_settings
		self.reset_stats()
		# Игра Alien Invasion запускатеся в неактивном состоянии
		self.game_active = False
		# Рекорд
		self.high_score = 0

	def reset_stats(self):
		# Инициализиурет статистику, изменяющуюся в ходе игры
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

