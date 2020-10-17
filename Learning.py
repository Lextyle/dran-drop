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
	def update(self, event, cells, pushers, rotaters):
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
								if is_collision(cell.x, cell.y, self.image.get_width(), self.image.get_height(), pusher.x, pusher.y, self.image.get_width(), self.image.get_height()):
									move_block = False
									break
						for rotater in rotaters:
							if is_collision(cell.x, cell.y, self.image.get_width(), self.image.get_height(), rotater.x, rotater.y, self.image.get_width(), self.image.get_height()):
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
						if pusher != self:
							if is_collision(self.last_pos[0], self.last_pos[1], self.image.get_width(), self.image.get_height(), pusher.x, pusher.y, self.image.get_width(), self.image.get_height()):
								move_block = False
								self.x = pusher.x - self.image.get_width() - ((pusher.x - self.image.get_width()) % self.image.get_width())
								self.y = pusher.y - self.image.get_height() - ((pusher.y - self.image.get_height()) % self.image.get_height())
								break
					for rotater in rotaters:
						if is_collision(self.last_pos[0], self.last_pos[1], self.image.get_width(), self.image.get_height(), rotater.x, rotater.y, self.image.get_width(), self.image.get_height()):
							move_block = False
							self.x = rotater.x - self.image.get_width() - ((rotater.x - self.image.get_width()) % self.image.get_width())
							self.y = rotater.y - self.image.get_height() - ((rotater.y - self.image.get_height()) % self.image.get_height())
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
	def move_block(self, pushers, rotaters):
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
	def update(self, event, cells, pushers, rotaters):
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
							if is_collision(cell.x, cell.y, self.image.get_width(), self.image.get_height(), pusher.x, pusher.y, self.image.get_width(), self.image.get_height()):
								move_block = False
								break
						for rotater in rotaters:
							if rotater != self:
								if is_collision(cell.x, cell.y, self.image.get_width(), self.image.get_height(), rotater.x, rotater.y, self.image.get_width(), self.image.get_height()):
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
					for rotater in rotaters:
						if rotater != self:
							if is_collision(self.last_pos[0], self.last_pos[1], self.image.get_width(), self.image.get_height(), rotater.x, rotater.y, self.image.get_width(), self.image.get_height()):
								move_block = False
								self.x = rotater.x - self.image.get_width() - ((rotater.x - self.image.get_width()) % self.image.get_width())
								self.y = rotater.y - self.image.get_height() - ((rotater.y - self.image.get_height()) % self.image.get_height())
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
pushers = [Pusher(40 * 9, 40 * 10, "RIGHT"), Pusher(40 * 10, 40 * 10, "LEFT"), Pusher(40 * 11, 40 * 10, "DOWN"), Pusher(40 * 11, 40 * 11, "UP")]
rotaters = [Rotater(80, 80), Rotater(40, 80), Rotater(0, 80), Rotater(120, 80)]
cells = []
y = 0
for i in range(window_height // pygame.image.load(r"images\image.png").get_height()):
	x = 0
	for i in range(window_width // pygame.image.load(r"images\image.png").get_width()):
		cells.append(Cell(x, y, pygame.image.load(r"images\image.png").get_width(), pygame.image.load(r"images\image.png").get_height()))
		x += pygame.image.load(r"images\image.png").get_width()
	y += pygame.image.load(r"images\image.png").get_height()
while True:
	window.fill((52, 52, 52))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		for pusher in pushers:
			pusher.update(event, cells, pushers, rotaters)
		for rotater in rotaters:
			rotater.update(event, cells, pushers, rotaters)
	for cell in cells:
		cell.draw(window)
	for pusher in pushers:
		pusher.move_block(pushers, rotaters)
	for rotater in rotaters:
		rotater.draw(window)
	for pusher in pushers:
		pusher.draw(window)
	pygame.display.update()