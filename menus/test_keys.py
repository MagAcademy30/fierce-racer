# By OrangeDogTeam, MG30.
# test_keys.py - Меню для теста тача, кнопок и геймпада.

import pygame, os, sys

from config import *
from scripts.tcursor import *
from scripts.button import *

class touchcircle:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.tcursor = kwargs["tcursor"]
		self.options = kwargs["options"]

		self.mashtab = int(self.options.get(0))

	def tick(self):
		for touch in self.tcursor.touch:
			pygame.draw.circle(self.screen, (0, 0, 150), self.tcursor.touch[touch], 50)

class test_keys:
	def __init__(self, args):
		self.screen = args["screen"]
		self.go = args["go"]
		self.go_previos = args["go_previos"]
		self.assets_import = args["assets_import"]
		self.path = args["path"]
		self.options = args["options"]

		self.mashtab = int(self.options.get(0))
		self.tcursor = tcursor(screen=self.screen)
		self.touchcircle = touchcircle(screen=self.screen, tcursor=self.tcursor, options=self.options)
		self.go_back_button = button(screen=self.screen, params=["Назад", (self.mashtab, self.screen.get_size()[1]-6*self.mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_back)

	def go_back(self):
		self.go_previos()

	def tick(self):
		self.screen.fill((255, 255, 255))

		self.go_back_button.tick()
		self.touchcircle.tick()

		for event in pygame.event.get():
			self.tcursor.event(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()