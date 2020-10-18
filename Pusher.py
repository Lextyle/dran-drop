from Collisions import *
from Sounds import *
from pygame.image import load as load_image
from pygame.transform import rotate as rotate_image
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
class Pusher():
	def __init__(self, x, y, direction):
		self.image = load_image(r"images\image.png")
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
		if event.type == MOUSEMOTION:
			if self.move:
				self.x += event.pos[0] - self.mouse_last_pos[0]
				self.y += event.pos[1] - self.mouse_last_pos[1]
				self.mouse_last_pos = event.pos
	def move_block(self, pushers, rotaters, enemies):
		if self.rotate:
			self.angle -= 1
			if self.angle <= 0:
				self.angle = 360
			if self.angle % 90 == 0:
				self.rotate = False
		else:
			if self.angle == 360:
				self.x += 1
				for pusher in pushers:
					if pusher != self:
						if is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.x -= 1
				for rotater in rotaters:
					if is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
						self.x -= 1
						self.rotate = True
			if self.angle == 270:
				self.y += 1
				for pusher in pushers:
					if pusher != self:
						if is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.y -= 1
				for rotater in rotaters:
					if is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
						self.y -= 1
						self.rotate = True
			if self.angle == 180:
				self.x -= 1
				for pusher in pushers:
					if pusher != self:
						if is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.x += 1
				for rotater in rotaters:
					if is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
						self.x += 1
						self.rotate = True
			if self.angle == 90:
				self.y -= 1
				for pusher in pushers:
					if pusher != self:
						if is_collision(pusher.x, pusher.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
							self.y += 1
				for rotater in rotaters:
					if is_collision(rotater.x, rotater.y, self.image.get_width(), self.image.get_height(), self.x, self.y, self.image.get_width(), self.image.get_height()):
						self.y += 1
						self.rotate = True
			for enemy in enemies:
				if is_collision(self.x, self.y, self.image.get_width(), self.image.get_height(), enemy.x, enemy.y, self.image.get_width(), self.image.get_height()):
					enemies.pop(enemies.index(enemy))
					pushers.pop(pushers.index(self))
					explosion_sound.play()
					break
	def draw(self, window):
		rotated_image = rotate_image(self.image, self.angle)
		window.blit(rotated_image, ((self.x + self.image.get_width() // 2) - rotated_image.get_width() // 2, (self.y + self.image.get_height() // 2) - rotated_image.get_height() // 2))	