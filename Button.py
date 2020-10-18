from pygame import MOUSEBUTTONDOWN
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.x = x
		self.y = y
		self.pressed = False
	def update(self, event):
		self.pressed = False
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0] in range(self.x, self.x + self.image.get_width()) and event.pos[1] in range(self.y, self.y + self.image.get_height()):
					self.pressed = True
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))