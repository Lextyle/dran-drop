from pygame.image import load as load_image
class Enemy():
	def __init__(self, x, y):
		self.image = load_image(r"images\enemy_image.png")
		self.x = x
		self.y = y
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))