import pygame
from pyautogui import size
def is_collision(x_1, y_1, width_1, height_1, x_2, y_2, width_2, height_2):
	return x_1 in range(x_2 + 1 - width_1, x_2 - 1 + width_2) and y_1 in range(y_2 + 1 - height_1, y_2 - 1 + height_2)
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
cells = [pygame.Surface((40, 40)), pygame.Surface((40, 40))]
cells_pos = [window_width // 2 - 40]
image = pygame.image.load(r"images\image.png")
image_x = window_width // 2 - image.get_width()
image_y = window_height // 2 - image.get_height() // 2
drag_sound = pygame.mixer.Sound("drag_sound.wav")
drop_sound = pygame.mixer.Sound("drop_sound.wav")
cells = []
cells_pos = []
y = 0 
for i in range(window_height // image.get_height()):
	x = 0
	for i in range(window_width // image.get_width()):
		cells.append(pygame.Surface((image.get_width(), image.get_height())))
		cells_pos.append([x, y])
		x += image.get_width()
	y += image.get_height()
for cell in cells:
	cell.fill((0, 0, 0))
	cell.set_alpha(60)
move_image = False
last_mouse_pos = [0, 0]
last_image_pos = [image_x, image_y]
while True:
	window.fill((52, 52, 52))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if not (move_image) and event.pos[0] in range(image_x, image_x + image.get_width()) and event.pos[1] in range(image_y, image_y + image.get_height()):
					last_mouse_pos = event.pos
					last_image_pos = [image_x, image_y]
					move_image = True
					drag_sound.play()
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				for cell_pos in cells_pos:
					is_pos_cange = False
					if cell_pos[0] != last_image_pos[0] or cell_pos[1] != last_image_pos[1]:
						if is_collision(cell_pos[0] + image.get_width() // 2, cell_pos[1] + image.get_height() // 2, 1, 1, image_x, image_y, image.get_width(), image.get_height()):
							image_x = cell_pos[0]
							image_y = cell_pos[1]
							is_pos_cange = True
							break
				if not is_pos_cange:
					image_x = last_image_pos[0]
					image_y = last_image_pos[1]
				if move_image:
					drop_sound.play()
				move_image = False
		if event.type == pygame.MOUSEMOTION:
			if move_image:
				image_x += event.pos[0] - last_mouse_pos[0]
				image_y += event.pos[1] - last_mouse_pos[1]
				last_mouse_pos = event.pos
	for index in range(len(cells)):
		pygame.draw.rect(window, (0, 0, 0), (cells_pos[index][0], cells_pos[index][1], image.get_width(), image.get_height()), 2)
		window.blit(cells[index], (cells_pos[index][0], cells_pos[index][1]))
	window.blit(image, (image_x, image_y))
	pygame.display.update()