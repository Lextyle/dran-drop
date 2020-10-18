try:
	import pygame
except:
	from os import system
	system("pip install pygame")
try:
	from pyautogui import size
except:
	from os import system
	system("pip install pyautogui")
def is_collision(x_1, y_1, width_1, height_1, x_2, y_2, width_2, height_2):
	return x_1 in range(x_2 + 1 - width_1, x_2 - 1 + width_2) and y_1 in range(y_2 + 1 - height_1, y_2 - 1 + height_2)
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
cells = []
cells_pos = []
drag_sound = pygame.mixer.Sound("drag_sound.wav")
drop_sound = pygame.mixer.Sound("drop_sound.wav")
explosion_sound = pygame.mixer.Sound("explosion_sound.wav")
cells = []
cells_pos = []
class Cell():
	def __init__(self, x, y, width, height):
		self.image = pygame.Surface((width, height))
		self.x = x
		self.y = y
		self.activated = False
	def draw(self, window):
		if self.activated:
			self.image.fill((0, 0, 0))
		else:
			self.image.fill((125, 125, 125))
		self.image.set_alpha(60)
		window.blit(self.image, (self.x, self.y))
		pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.image.get_width(), self.image.get_height()), 2)
class Pusher():
	def __init__(self, x, y, direction):
		self.image = pygame.image.load(r"images\image.png")
		self.x = x
		self.y = y
		if direction == "RIGHT":
			self.angle = 0
		if direction == "DOWN":
			self.angle = 270
		if direction == "LEFT":
			self.angle = 180
		if direction == "UP":
			self.angle = 90
		self.move = False
		self.mouse_last_pos = [0, 0]
		self.rotate = False
	def update(self, event, cells, pushers, rotaters, enemies):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if is_collision(event.pos[0], event.pos[1], 0, 0, self.x, self.y, self.image.get_width(), self.image.get_height()):
				self.move = True
				self.mouse_last_pos = event.pos
				self.last_pos = [self.x, self.y]
				drag_sound.play()
		if event.type == pygame.MOUSEBUTTONUP:
			if self.move:
				block_moved = False
				for cell in cells:
					if is_collision(self.x, self.y, self.image.get_width(), self.image.get_height(), cell.x + self.image.get_width() // 2, cell.y + self.image.get_height() // 2, 1, 1):
						move_block = True
						for pusher in pushers:
							if pusher != self:
								if pusher.x == cell.x and pusher.y == cell.y:
									move_block = False
									break
						for rotater in rotaters:
							if rotater.x == cell.x and rotater.y == cell.y:
								move_block = False
								break
						for enemy in enemies:
							if enemy.x == cell.x and enemy.y == cell.y:
								move_block = False
								break
						if move_block:
							self.x = cell.x
							self.y = cell.y
							block_moved = True
							drop_sound.play()
						break
				if not block_moved:
					self.x = self.last_pos[0]
					self.y = self.last_pos[1]
					drop_sound.play()
				self.move = False
		if event.type == pygame.MOUSEMOTION:
			if self.move:
				self.x += event.pos[0] - self.mouse_last_pos[0]
				self.y += event.pos[1] - self.mouse_last_pos[1]
				self.mouse_last_pos = event.pos
	def move_block(self, pushers, rotaters, enemies):
		if not self.move:
			if self.rotate:
				self.angle += 1
				if self.angle == 360:
					self.angle = 0
				if self.angle % 90 == 0 or self.angle == 0:
					self.rotate = False
			else:
				if self.angle == 0:
					self.x += 1
					for pusher in pushers:
						if pusher != self:
							if not (pusher.move) and is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
								self.x -= 1
					for rotater in rotaters:
						if not (rotater.move) and is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.x -= 1
							self.rotate = True
				if self.angle == 270:
					self.y += 1
					for pusher in pushers:
						if pusher != self:
							if not (pusher.move) and is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
								self.y -= 1
					for rotater in rotaters:
						if not (rotater.move) and is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.y -= 1
							self.rotate = True
				if self.angle == 180:
					self.x -= 1
					for pusher in pushers:
						if pusher != self:
							if not (pusher.move) and is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
								self.x += 1
					for rotater in rotaters:
						if not (rotater.move) and is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.x += 1
							self.rotate = True
				if self.angle == 90:
					self.y -= 1
					for pusher in pushers:
						if pusher != self:
							if not (pusher.move) and is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
								self.y += 1
					for rotater in rotaters:
						if not (rotater.move) and is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.y += 1
							self.rotate = True
				for enemy in enemies:
					if is_collision(self.x, self.y, self.image.get_width(), self.image.get_height(), enemy.x, enemy.y, self.image.get_width(), self.image.get_height()):
						enemies.pop(enemies.index(enemy))
						pushers.pop(pushers.index(self))
						explosion_sound.play()
						break
	def draw(self, window):
		rotated_image = pygame.transform.rotate(self.image, self.angle)
		window.blit(rotated_image, ((self.x + self.image.get_width() // 2) - rotated_image.get_width() // 2, (self.y + self.image.get_height() // 2) - rotated_image.get_height() // 2))	
class Rotater():
	def __init__(self, x, y):
		self.image = pygame.image.load(r"images\rotater_image.png")
		self.x = x
		self.y = y
		self.last_pos = [self.x, self.y]
		self.angle = 0
		self.move = False
	def update(self, event, cells, pushers, rotaters, enemies):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if is_collision(event.pos[0], event.pos[1], 0, 0, self.x, self.y, self.image.get_width(), self.image.get_height()):
				self.move = True
				self.mouse_last_pos = event.pos
				self.last_pos = [self.x, self.y]
				drag_sound.play()
		if event.type == pygame.MOUSEBUTTONUP:
			if self.move:
				block_moved = False
				for cell in cells:
					if is_collision(self.x, self.y, self.image.get_width(), self.image.get_height(), cell.x + self.image.get_width() // 2, cell.y + self.image.get_height() // 2, 1, 1):
						move_block = True
						for pusher in pushers:
							if pusher.x == cell.x and pusher.y == cell.y:
								move_block = False
								break
						for rotater in rotaters:
							if rotater != self:
								if rotater.x == cell.x and rotater.y == cell.y:
									move_block = False
									break
						for enemy in enemies:
							if enemy.x == cell.x and enemy.y == cell.y:
								move_block = False
								break
						if move_block:
							self.x = cell.x
							self.y = cell.y
							block_moved = True
							drop_sound.play()
						break
				if not block_moved:
					move_block = True
					for pusher in pushers:
						if is_collision(self.last_pos[0], self.last_pos[1], self.image.get_width(), self.image.get_height(), pusher.x, pusher.y, self.image.get_width(), self.image.get_height()):
							move_block = False
							self.x = pusher.x - self.image.get_width() - ((pusher.x - self.image.get_width()) % self.image.get_width())
							self.y = pusher.y - self.image.get_height() - ((pusher.y - self.image.get_height()) % self.image.get_height())
							break
					if move_block:
						self.x = self.last_pos[0]
						self.y = self.last_pos[1]
					drop_sound.play()
				self.move = False
		if event.type == pygame.MOUSEMOTION:
			if self.move:
				self.x += event.pos[0] - self.mouse_last_pos[0]
				self.y += event.pos[1] - self.mouse_last_pos[1]
				self.mouse_last_pos = event.pos
	def draw(self, window):
		rotated_image = pygame.transform.rotate(self.image, self.angle)
		window.blit(rotated_image, ((self.x + self.image.get_width() // 2) - rotated_image.get_width() // 2, (self.y + self.image.get_height() // 2) - rotated_image.get_height() // 2))
class Enemy():
	def __init__(self, x, y):
		self.image = pygame.image.load(r"images\enemy_image.png")
		self.x = x
		self.y = y
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.x = x
		self.y = y
		self.pressed = False
	def update(self, event):
		self.pressed = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0] in range(self.x, self.x + self.image.get_width()) and event.pos[1] in range(self.y, self.y + self.image.get_height()):
					self.pressed = True
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))
cells = []
y = 0
for i in range(window_height // pygame.image.load(r"images\image.png").get_height()):
	x = 0
	for i in range(window_width // pygame.image.load(r"images\image.png").get_width()):
		cells.append(Cell(x, y, pygame.image.load(r"images\image.png").get_width(), pygame.image.load(r"images\image.png").get_height()))
		x += pygame.image.load(r"images\image.png").get_width()
	y += pygame.image.load(r"images\image.png").get_height()
def level_3():
	pushers = [Pusher(40 * 9, 40 * 10, "LEFT")]
	rotaters = [Rotater(80, 80), Rotater(40+, 80)]
	enemies = [Enemy(window_width - 40, 40 * 10)]
	play = False
	play_button_image = pygame.image.load(r"images\play_button.png")
	next_button_image = pygame.image.load(r"images\next_button.png")
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image)
	create_next_button = False
	while True:
		window.fill((52, 52, 52))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
				play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			play = True
		if next_button.pressed:
			pygame.quit()
		for cell in cells:
			cell.draw(window)
		if play:
			for pusher in pushers:
				pusher.move_block(pushers, rotaters, enemies)
		for rotater in rotaters:
			rotater.draw(window)
		for pusher in pushers:
			pusher.draw(window)
		if not play:
			play_button.draw(window)
		for enemy in enemies:
			enemy.draw(window)
		if create_next_button:
			next_button.draw(window)
		if pushers == []:
			create_next_button = True
		pygame.display.update()
def level_2():
	pushers = [Pusher(40 * 9, 40 * 10, "DOWN"), Pusher(40 * 10, 40 * 10, "DOWN")]
	rotaters = [Rotater(80, 80)]
	enemies = [Enemy(40 * 5, 40 * 10), Enemy(40, 0)]
	play = False
	play_button_image = pygame.image.load(r"images\play_button.png")
	next_button_image = pygame.image.load(r"images\next_button.png")
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image)
	create_next_button = False
	while True:
		window.fill((52, 52, 52))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
				play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			play = True
		if next_button.pressed:
			level_3()
		for cell in cells:
			cell.draw(window)
		if play:
			for pusher in pushers:
				pusher.move_block(pushers, rotaters, enemies)
		for rotater in rotaters:
			rotater.draw(window)
		for pusher in pushers:
			pusher.draw(window)
		if not play:
			play_button.draw(window)
		for enemy in enemies:
			enemy.draw(window)
		if create_next_button:
			next_button.draw(window)
		if pushers == []:
			create_next_button = True
		pygame.display.update()
def level_1():
	pushers = [Pusher(40 * 9, 40 * 10, "LEFT"), Pusher(40 * 10, 40 * 10, "DOWN")]
	rotaters = [Rotater(80, 80), Rotater(40, 80)]
	enemies = [Enemy(window_width - 40, window_height - 40), Enemy(window_width - 40, 0)]
	play = False
	play_button_image = pygame.image.load(r"images\play_button.png")
	next_button_image = pygame.image.load(r"images\next_button.png")
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image)
	create_next_button = False
	while True:
		window.fill((52, 52, 52))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
				play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			play = True
		if next_button.pressed:
			level_2()
			print("a")
		for cell in cells:
			cell.draw(window)
		if play:
			for pusher in pushers:
				pusher.move_block(pushers, rotaters, enemies)
		for rotater in rotaters:
			rotater.draw(window)
		for pusher in pushers:
			pusher.draw(window)
		if not play:
			play_button.draw(window)
		for enemy in enemies:
			enemy.draw(window)
		if create_next_button:
			next_button.draw(window)
		if pushers == []:
			create_next_button = True
		pygame.display.update()
level_1()