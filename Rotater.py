from Collisions import *
from Sounds import *
from pygame.image import load as load_image
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
class Rotater():
	def __init__(self, x, y):
		self.image = load_image(r"images\rotater_image.png")
		self.x = x
		self.y = y
		self.last_pos = [self.x, self.y]
		self.move = False
	def update(self, event, cells, pushers, rotaters, enemies):
		if event.type == MOUSEBUTTONDOWN:
			if is_collision(event.pos[0], event.pos[1], 0, 0, self.x, self.y, self.image.get_width(), self.image.get_height()):
				self.move = True
				self.mouse_last_pos = event.pos
				self.last_pos = [self.x, self.y]
				drag_sound.play()
		if event.type == MOUSEBUTTONUP:
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
					self.x = self.last_pos[0]
					self.y = self.last_pos[1]
					drop_sound.play()
				self.move = False
		if event.type == MOUSEMOTION:
			if self.move:
				self.x += event.pos[0] - self.mouse_last_pos[0]
				self.y += event.pos[1] - self.mouse_last_pos[1]
				self.mouse_last_pos = event.pos
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))