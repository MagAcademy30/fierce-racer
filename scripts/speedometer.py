# By OrangeDog Team, MG30
# speedometer.py - Спидометр игрока.

import pygame, os, sys

from config import *

class speedometer:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.player = kwargs["player"]
		self.path = kwargs["path"]
		self.options = kwargs["options"]
		self.mashtab = int(self.options.get(0))
		self.font = pygame.font.Font(self.path+font_path, 3*self.mashtab)

	def tick(self):
		text = self.font.render("Скорость: "+str(round(self.player.speed)), 0, (255, 255, 255))
		self.screen.blit(text, (self.mashtab, self.screen.get_size()[1]-text.get_size()[1]-self.mashtab))