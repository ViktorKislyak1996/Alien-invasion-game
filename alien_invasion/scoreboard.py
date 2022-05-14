import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
	# Класс для вывода игровой информации
	def __init__(self, ai_settings, screen, stats):
		# Инициализирует атрибуты подсчета очков
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = screen.get_rect()
		self.stats = stats

		# Настройки шрифта для вывода счета
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)
		# Подготовка изображений счетов
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		# Преобразует текущий счет в графическое изображение
		rounded_score = round(self.stats.score, -1)
		score_str = '{:,}'.format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.ai_settings.bg_color)
		# Вывод счета в правой вехрней части экрана
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		# Преобразует рекорд в изображение
		high_score = round(self.stats.high_score, -1)
		high_score_str = '{:,}'.format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color,
			self.ai_settings.bg_color)
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20

	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
			self.ai_settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		# Сообщает количество оставшихся кораблей
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.image = pygame.transform.scale(ship.image, (30, 25))
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		# Вывод счета на экран
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# Вывод кораблей
		self.ships.draw(self.screen)
