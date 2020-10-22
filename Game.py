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
from Cell import *
from Rotater import *
from Pusher import *
from Button import *
from Enemy import *
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
cells = []
y = 0
for i in range(window_height // pygame.image.load(r"images\pusher_image.png").get_height()):
	x = 0
	for i in range(window_width // pygame.image.load(r"images\pusher_image.png").get_width()):
		cells.append(Cell(x, y, pygame.image.load(r"images\pusher_image.png").get_width(), pygame.image.load(r"images\pusher_image.png").get_height()))
		x += pygame.image.load(r"images\pusher_image.png").get_width()
	y += pygame.image.load(r"images\pusher_image.png").get_height()
play_button_image = pygame.image.load(r"images\play_button.png")
next_button_image = pygame.image.load(r"images\next_button.png")
restart_button_image = pygame.image.load(r"images\restart_image.png")
menu_buttons_width = pygame.image.load(r"images\play_button_image.png").get_width() * 2
menu_buttons_height = pygame.image.load(r"images\play_button_image.png").get_height() * 2
menu_play_button_image = pygame.transform.scale(pygame.image.load(r"images\play_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_hover_play_button_image = pygame.transform.scale(pygame.image.load(r"images\hover_play_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_settings_button_image = pygame.transform.scale(pygame.image.load(r"images\settings_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_hover_settings_button_image = pygame.transform.scale(pygame.image.load(r"images\hover_settings_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_exit_button_image = pygame.transform.scale(pygame.image.load(r"images\exit_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_hover_exit_button_image = pygame.transform.scale(pygame.image.load(r"images\hover_exit_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_button_image = pygame.transform.scale(pygame.image.load(r"images\menu_button_image.png"), (menu_buttons_width, menu_buttons_height))
hover_menu_button_image = pygame.transform.scale(pygame.image.load(r"images\hover_menu_button_image.png"), (menu_buttons_width, menu_buttons_height))
menu_buttons_num = 3
def level_3():
	pushers = [Pusher(40 * 9, 40 * 10, "LEFT")]
	rotaters = [Rotater(80, 80), Rotater(40, 80)]
	enemies = [Enemy(window_width - 40, 40 * 10)]
	play = False
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image)
	create_next_button = False
	while True:
		window.fill((52, 52, 52))
		play_button.pressed = False
		next_button.pressed = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					menu(True)
			play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			button_pressed_sound.play()
			if play:
				level_3()
			else:
				play = True
				play_button.not_hover_image = restart_button_image
				play_button.hover_image = restart_button_image
		if next_button.pressed:
			button_pressed_sound.play()
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
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image)
	create_next_button = False
	while True:
		window.fill((52, 52, 52))
		play_button.pressed = False
		next_button.pressed = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					menu(True)
			play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			button_pressed_sound.play()
			if play:
				level_2()
			else:
				play = True
				play_button.not_hover_image = restart_button_image
				play_button.hover_image = restart_button_image
		if next_button.pressed:
			button_pressed_sound.play()
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
	play_button = Button(20, (window_height - 20) - play_button_image.get_height(), play_button_image, play_button_image)
	next_button = Button((window_width - next_button_image.get_width()) - 20, (window_height - 20) - next_button_image.get_height(), next_button_image, next_button_image)
	create_next_button = False
	show_menu = False
	while True:
		window.fill((52, 52, 52))
		play_button.pressed = False
		next_button.pressed = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if not play:
				for pusher in pushers:
					pusher.update(event, cells, pushers, rotaters, enemies)
				for rotater in rotaters:
					rotater.update(event, cells, pushers, rotaters, enemies)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					show_menu = True
			play_button.update(event)
			if create_next_button:
				next_button.update(event)
		if play_button.pressed:
			button_pressed_sound.play()
			if play:
				level_1()
			else:
				play = True
				play_button.not_hover_image = restart_button_image
				play_button.hover_image = restart_button_image
		if next_button.pressed:
			button_pressed_sound.play()
			level_2()
		for cell in cells:
			cell.draw(window)
		if play:
			for pusher in pushers:
				pusher.move_block(pushers, rotaters, enemies)
		for rotater in rotaters:
			rotater.draw(window)
		for pusher in pushers:
			pusher.draw(window)
		play_button.draw(window)
		for enemy in enemies:
			enemy.draw(window)
		if create_next_button:
			next_button.draw(window)
		if pushers == []:
			create_next_button = True
		pygame.display.update()
		if show_menu:
			menu(True)
			show_menu = False
def game():
	level_1()
def settings(in_game):
	jump_height = 10
	Surface_width = 150
	Surface_height = menu_buttons_height * menu_buttons_num + jump_height * (menu_buttons_num - 1)
	Surface_x = window_width // 2 - Surface_width // 2
	Surface_y = window_height // 2 - Surface_height // 2
	menu_button = Button(Surface_x + 10, Surface_y + 10, pygame.transform.scale(menu_button_image, (menu_buttons_width // 2, menu_buttons_height // 2)), pygame.transform.scale(hover_menu_button_image, (menu_buttons_width // 2, menu_buttons_height // 2)))
	while True:
		pygame.draw.rect(window, (60, 60, 60), (Surface_x, Surface_y, Surface_width, Surface_height))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			menu_button.update(event)
		if menu_button.pressed:
			break
		menu_button.draw(window)
		pygame.display.update()
def menu(in_game = False):
	jump_height = 10
	Surface_width = 150
	Surface_height = menu_buttons_height * menu_buttons_num + jump_height * (menu_buttons_num - 1)
	Surface_x = window_width // 2 - Surface_width // 2
	Surface_y = window_height // 2 - Surface_height // 2
	buttons_x = Surface_x + (Surface_width // 2 - menu_buttons_width // 2)
	play_button = Button(buttons_x, Surface_y, menu_play_button_image, menu_hover_play_button_image)
	settings_button = Button(buttons_x, play_button.y + menu_buttons_height + jump_height, menu_settings_button_image, menu_hover_settings_button_image)
	exit_button = Button(buttons_x, settings_button.y + menu_buttons_height + jump_height, menu_exit_button_image, menu_hover_exit_button_image)
	if in_game:
		black_Surface = pygame.Surface((window_width, window_height))
		black_Surface.fill((0, 0, 0))
		black_Surface.set_alpha(50)
		window.blit(black_Surface, (0, 0))
	while True:
		settings_button.pressed = False
		if not in_game:
			window.fill((33, 33, 33))
		pygame.draw.rect(window, (60, 60, 60), (Surface_x, Surface_y, Surface_width, Surface_height))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			play_button.update(event)
			settings_button.update(event)
			exit_button.update(event)
		if play_button.pressed:
			button_pressed_sound.play()
			if in_game:
				break
			else:
				game()
		if settings_button.pressed:
			button_pressed_sound.play()
			settings(in_game)
		if exit_button.pressed:
			button_pressed_sound.play()
			pygame.quit()
		play_button.draw(window)
		settings_button.draw(window)
		exit_button.draw(window)
		pygame.display.update()
menu()