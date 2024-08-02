# By OrangeDog Team, MG30.
# Меню menus/intro.py показывает логотип OrangeDog Team и прочие штуки которые нужно показать перед началом игры.

import pygame, os, sys, time
from config import *
from scripts.fading import *

class intro:
	def __init__(self, args):
		self.screen = args["screen"]
		self.assets_import = args["assets_import"]
		self.go = args["go"]
		self.team_logo = self.assets_import.get_texture()["intro"]["orangedogteam_logo"]
		self.pygame_powered_logo = self.assets_import.get_texture()["intro"]["pygame_powered_logo"]

		self.team_logo_fading = fading(screen=self.screen, surface=self.team_logo, pos=(self.screen.get_size()[0]/2-self.team_logo.get_size()[0]/2, self.screen.get_size()[1]/2-self.team_logo.get_size()[1]/2), speed=8)
		self.pygame_powered_logo_fading = fading(screen=self.screen, surface=self.pygame_powered_logo, pos=(self.screen.get_size()[0]/2-self.pygame_powered_logo.get_size()[0]/2, self.screen.get_size()[1]/2-self.pygame_powered_logo.get_size()[1]/2), speed=8)
		
		self.fade = 0 # 0 - fade_in, 1 - fade_out
		self.fade_logos = [self.team_logo_fading, self.pygame_powered_logo_fading]
		self.fade_logo = 0
		self.fade_logo_max = 0

	def tick(self):
		self.screen.fill((0, 0, 0))
		
		self.fade_logos[self.fade_logo].tick()

		if self.fade == 0:
			self.fade_logos[self.fade_logo].fade_in()

		elif self.fade == 2:
			time.sleep(1)
			self.fade = 1

		elif self.fade == 1:
			self.fade_logos[self.fade_logo].fade_out()
			if self.fade_logos[self.fade_logo].fade_level <= 0:
				if self.fade_logo >= self.fade_logo_max:
					self.go(1)
				else:
					self.fade_logo += 1
					self.fade = 0

		if self.fade_logos[self.fade_logo].fade_level >= self.fade_logos[self.fade_logo].fade_max and self.fade == 0:
			self.fade = 2

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()