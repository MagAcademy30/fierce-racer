# By OrangeDog Team, MG30
# main_menu.py - Главное меню игры

import pygame, os, sys, random

from config import *
from scripts.fading import *
from scripts.background import *
from scripts.button import *
from scripts.tcursor import *
from scripts.road import *
from scripts.player import *

class main_menu:
	def __init__(self, args):
		self.screen = args["screen"]
		self.go = args["go"]
		self.assets_import = args["assets_import"]
		self.path = args["path"]
		self.options = args["options"]

		mashtab = int(self.options.get(0))
		self.black_screen_fade = fading(screen=self.screen, surface=pygame.Surface(self.screen.get_size()), pos=(0, 0), speed=15)
		self.black_screen_fade.fade_level = self.black_screen_fade.fade_max
		self.background = background(screen=self.screen, surface=self.assets_import.get_texture()["bg"]["bg_default"])
		self.background.speed = 5
		#self.road = road(screen=self.screen, background=self.background, player=self.player, assets_import=self.assets_import, options=self.options)
		self.tcursor = tcursor(screen=self.screen)
		#self.test_1 = button(screen=self.screen, params=["Test 1", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.bobik)
		self.play_button = button(screen=self.screen, params=["Играть", (57*mashtab+self.background.bg_x, 45*mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_game)
		self.options_button = button(screen=self.screen, params=["Настройки", (53*mashtab+self.background.bg_x, 51*mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_options)
		self.exit_button = button(screen=self.screen, params=["Выйти", (59*mashtab+self.background.bg_x, 57*mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.exit)
		self.test_keys_button = button(screen=self.screen, params=["Tests", (mashtab, mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_debug)

	def go_debug(self):
		self.go(2)

	def go_game(self):
		self.go(3)

	def go_options(self):
		self.go(4)

	def exit(self):
		pygame.quit()
		sys.exit()

	def tick(self):
		self.screen.fill((0, 0, 0))
		
		self.background.tick()
		self.play_button.tick()
		self.options_button.tick()
		self.exit_button.tick()
		if debug:
			self.test_keys_button.tick()

		self.black_screen_fade.fade_out()
		self.black_screen_fade.tick()

		for event in pygame.event.get():
			self.tcursor.event(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()