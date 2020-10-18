from pygame import Surface
from pygame.draw import rect as draw_rect
class Cell():
	def __init__(self, x, y, width, height):
		self.image = Surface((width, height))
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
		draw_rect(window, (0, 0, 0), (self.x, self.y, self.image.get_width(), self.image.get_height()), 2)