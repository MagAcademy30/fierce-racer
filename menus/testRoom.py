# By OrangeDog Team, MG30.
# menus/testRoom.py сделан как "example".
#e
# testRoom и все меню в игре сделаны так:
# class имя:
# 	def __init__(self, args):
# 		инициализация меню
# 	def tick(self):
# 		будет вызыватся бесконечным циклом, тут же и работаем.

import pygame, os, sys, random
from scripts.joystick_controls import *
from scripts.tcursor import *

class testRoom:
	def __init__(self, args):
		# см. main.py на счёт args.
		self.screen = args["screen"] # Берём surface окна.
		#self.joy = joystick_controls()
		self.tcursor = tcursor(screen=self.screen)
	def bobik(self): print(random.randint(0, 10))

	def tick(self):
		self.screen.fill((0, 0, 0))

		#self.joy.tick()

		# Важно! без event окно просто зависнет, так что он нам очень нужен.(Да и к тому-же а как закрыть-то без него?)
		for event in pygame.event.get():
			self.tcursor.event(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()