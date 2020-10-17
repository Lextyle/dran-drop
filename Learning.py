try:
	import pygame
except:
	from os import system
	system("pip install pygame")
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
rotater_image = pygame.image.load(r"images\rotater_image.png")
rotater_image_x = 40
rotater_image_y = 40
block_image = pygame.image.load(r"images\block_image.png")
block_image_x = 40
block_image_y = 80
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
last_mouse_pos = [0, 0]
last_image_pos = [image_x, image_y]
last_rotater_image_pos = [rotater_image_x, rotater_image_y]
last_block_image_pos = [block_image_x, block_image_y]
angle = 0
change_angle = False
move_image = False
move_rotater_image = False
move_block_image = False
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
				if not (move_rotater_image) and event.pos[0] in range(rotater_image_x, rotater_image_x + rotater_image.get_width()) and event.pos[1] in range(rotater_image_y, rotater_image_y + rotater_image.get_height()):
					last_mouse_pos = event.pos
					last_rotater_image_pos = [rotater_image_x, rotater_image_y]
					move_rotater_image = True
					drag_sound.play()
				if not (move_block_image) and event.pos[0] in range(block_image_x, block_image_x + block_image.get_width()) and event.pos[1] in range(block_image_y, block_image_y + block_image.get_height()):
					last_mouse_pos = event.pos
					last_block_image_pos = [block_image_x, block_image_y]
					move_block_image = True
					drag_sound.play()
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if move_image:
					for cell_pos in cells_pos:
						is_pos_cange = False
						if cell_pos[0] != last_image_pos[0] or cell_pos[1] != last_image_pos[1]:
							if (not ((rotater_image_x == cell_pos[0] and rotater_image_y == cell_pos[1]) or is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), cell_pos[0], cell_pos[1], image.get_width(), image.get_height()))) and is_collision(cell_pos[0] + image.get_width() // 2, cell_pos[1] + image.get_height() // 2, 1, 1, image_x, image_y, image.get_width(), image.get_height()):
								image_x = cell_pos[0]
								image_y = cell_pos[1]
								is_pos_cange = True
								break
					if not is_pos_cange:
						image_x = last_image_pos[0]
						image_y = last_image_pos[1]
					drop_sound.play()
					move_image = False
				if move_rotater_image:
					for cell_pos in cells_pos:
						is_pos_cange = False
						if cell_pos[0] != last_rotater_image_pos[0] or cell_pos[1] != last_rotater_image_pos[1]:
							if (not (is_collision(image_x, image_y, image.get_width(), image.get_height(), cell_pos[0], cell_pos[1], image.get_width(), image.get_height()) or is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), cell_pos[0], cell_pos[1], image.get_width(), image.get_height()))) and is_collision(cell_pos[0] + rotater_image.get_width() // 2, cell_pos[1] + rotater_image.get_height() // 2, 1, 1, rotater_image_x, rotater_image_y, rotater_image.get_width(), rotater_image.get_height()):
								rotater_image_x = cell_pos[0]
								rotater_image_y = cell_pos[1]
								is_pos_cange = True
								break
					if not is_pos_cange:
						rotater_image_x = last_rotater_image_pos[0]
						rotater_image_y = last_rotater_image_pos[1]
					drop_sound.play()
					move_rotater_image = False
				if move_block_image:
					for cell_pos in cells_pos:
						is_pos_cange = False
						if cell_pos[0] != last_block_image_pos[0] or cell_pos[1] != last_block_image_pos[1]:
							if (not (is_collision(image_x, image_y, image.get_width(), image.get_height(), cell_pos[0], cell_pos[1], image.get_width(), image.get_height()) or (rotater_image_x == cell_pos[0] and rotater_image_y == cell_pos[1]))) and is_collision(cell_pos[0] + block_image.get_width() // 2, cell_pos[1] + block_image.get_height() // 2, 1, 1, block_image_x, block_image_y, block_image.get_width(), block_image.get_height()):
								block_image_x = cell_pos[0]
								block_image_y = cell_pos[1]
								is_pos_cange = True
								break
					if not is_pos_cange:
						block_image_x = last_block_image_pos[0]
						block_image_y = last_block_image_pos[1]
					drop_sound.play()
					move_block_image = False
		if event.type == pygame.MOUSEMOTION:
			if move_image:
				image_x += event.pos[0] - last_mouse_pos[0]
				image_y += event.pos[1] - last_mouse_pos[1]
				last_mouse_pos = event.pos
			if move_rotater_image:
				rotater_image_x += event.pos[0] - last_mouse_pos[0]
				rotater_image_y += event.pos[1] - last_mouse_pos[1]
				last_mouse_pos = event.pos
			if move_block_image:
				block_image_x += event.pos[0] - last_mouse_pos[0]
				block_image_y += event.pos[1] - last_mouse_pos[1]
				last_mouse_pos = event.pos
	for index in range(len(cells)):
		pygame.draw.rect(window, (0, 0, 0), (cells_pos[index][0], cells_pos[index][1], image.get_width(), image.get_height()), 2)
		window.blit(cells[index], (cells_pos[index][0], cells_pos[index][1]))
	if change_angle:
		angle += 1
		if angle == 360:
			angle = 0
		if angle % 90 == 0 or angle == 0:
			change_angle = False
	if not (move_image or change_angle):
		if angle == 0:
			image_x += 1
			if not (move_block_image) and is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				block_image_x += 1
				if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), block_image_x, block_image_y, image.get_width(), image.get_height()):
					block_image_x -= 1
					image_x -= 1
			if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				image_x -= 1
				change_angle = True
		if angle == 270:
			image_y += 1
			if not (move_block_image) and is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				block_image_y += 1
				if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), block_image_x, block_image_y, image.get_width(), image.get_height()):
					block_image_y -= 1
					image_y -= 1
			if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				image_y -= 1
				change_angle = True
		if angle == 180:
			image_x -= 1
			if not (move_block_image) and is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				block_image_x -= 1
				if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), block_image_x, block_image_y, image.get_width(), image.get_height()):
					block_image_x += 1
					image_x += 1
			if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				image_x += 1
				change_angle = True
		if angle == 90:
			image_y -= 1
			if not (move_block_image) and is_collision(block_image_x, block_image_y, block_image.get_width(), block_image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				block_image_y -= 1
				if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), block_image_x, block_image_y, image.get_width(), image.get_height()):
					block_image_y += 1
					image_y += 1
			if not (move_rotater_image) and is_collision(rotater_image_x, rotater_image_y, image.get_width(), image.get_height(), image_x, image_y, image.get_width(), image.get_height()):
				image_y += 1
				change_angle = True
	rotated_image = pygame.transform.rotate(image, angle)
	window.blit(block_image, (block_image_x, block_image_y))
	window.blit(rotated_image, ((image_x + image.get_width() // 2) - rotated_image.get_width() // 2, (image_y + image.get_height() // 2) - rotated_image.get_height() // 2))
	window.blit(rotater_image, (rotater_image_x, rotater_image_y))
	pygame.display.update()