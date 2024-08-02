# By OrangeDog Team, MG30.
# scripts/assets_import.py содержит класс который импортирует все ассеты игры.

import pygame, os, sys

from config import *

class assets_import:
	def __init__(self, options, path):
		self.path = path
		self.options = options
		self.imported_sound = {}
		self.imported_texture = {}

		for a in paths_to_texture:
			self.imported_texture[a] = {}
			for b in paths_to_texture[a]:
				texture = pygame.image.load(self.path+paths_to_texture[a][b]).convert_alpha()
				if b == "orangedogteam_logo":
					texture = pygame.transform.scale(texture, (60*int(self.options.get(0)), 10*int(self.options.get(0))))
				elif b == "pygame_powered_logo":
					texture = pygame.transform.scale(texture, (70*int(self.options.get(0)), 25*int(self.options.get(0))))
				elif b == "button":
					#texture = pygame.transform.scale(texture, (12*int(self.options.get(0)), 12*int(self.options.get(0))))
					pass
				else:
					texture = pygame.transform.scale(texture, (texture.get_size()[0]*int(self.options.get(0)), texture.get_size()[1]*int(self.options.get(0))))
				self.imported_texture[a][b] = texture

		for a in paths_to_sound:
			self.imported_sound[a] = {}
			for b in paths_to_sound[a]:
				sound = pygame.mixer.Sound(self.path+paths_to_sound[a][b])
				self.imported_sound[a][b] = sound

	def get_sound(self):
		return self.imported_sound

	def get_texture(self):
		return self.imported_texture