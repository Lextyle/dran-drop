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
for i in range(window_height // pygame.image.load(r"images\image.png").get_height()):
	x = 0
	for i in range(window_width // pygame.image.load(r"images\image.png").get_width()):
		cells.append(Cell(x, y, pygame.image.load(r"images\image.png").get_width(), pygame.image.load(r"images\image.png").get_height()))
		x += pygame.image.load(r"images\image.png").get_width()
	y += pygame.image.load(r"images\image.png").get_height()
def level_3():
	pushers = [Pusher(40 * 9, 40 * 10, "LEFT")]
	rotaters = [Rotater(80, 80), Rotater(40, 80)]
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