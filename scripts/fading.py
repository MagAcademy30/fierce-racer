# By OrangeDog Team, MG30
# scripts/fading.py имеет одну простую вещь, и это работа с потуханием и появлением обьектов.
# Это можно использовать для вспышки и тд.

import pygame, os, sys

class fading:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		surface = kwargs["surface"]
		self.pos = kwargs["pos"]
		self.speed = kwargs["speed"]

		self.fade_level = 0
		self.fade_max = 300

		self.surface = pygame.Surface(surface.get_size())
		self.surface.blit(surface, (0, 0))
		self.surface.set_alpha(self.fade_level)

	def fade_in(self):
		if self.fade_level < self.fade_max:
			self.fade_level += self.speed
		self.surface.set_alpha(self.fade_level)

	def fade_out(self):
		if self.fade_level >= 0:
			self.fade_level -= self.speed
		self.surface.set_alpha(self.fade_level)

	def tick(self):
		self.screen.blit(self.surface, self.pos)