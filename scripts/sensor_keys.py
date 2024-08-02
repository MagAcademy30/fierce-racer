# By OrangeDog Team, MG30
# sensor_keys.py - Сенсорное управление.

import pygame, os, sys

from config import *

class sensor_keys:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.assets_import = kwargs["assets_import"]
		self.path = kwargs["path"]
		self.options = kwargs["options"]
		self.tcursor = kwargs["tcursor"]

		self.mashtab = int(self.options.get(0))
		self.size = int(self.options.get(4))
		self.font = pygame.font.Font(self.path+font_path, int(self.size*self.mashtab))
		self.key_imj = self.assets_import.get_texture()["gui"]["button"]
		self.key_imj = pygame.transform.scale(self.key_imj, (int(10*self.size*self.mashtab/2), int(10*self.size*self.mashtab/2)))

		self.key_left = pygame.Surface(self.key_imj.get_size(), pygame.SRCALPHA, 32).convert_alpha()
		text = self.font.render("<", 0, (147, 147, 147))
		self.key_left.blit(self.key_imj, (0, 0))
		self.key_left.blit(text, (self.key_left.get_size()[0]/2-text.get_size()[0]/2, self.key_left.get_size()[1]/2-text.get_size()[1]/2))

		self.key_right = pygame.Surface(self.key_imj.get_size(), pygame.SRCALPHA, 32).convert_alpha()
		text = self.font.render(">", 0, (147, 147, 147))
		self.key_right.blit(self.key_imj, (0, 0))
		self.key_right.blit(text, (self.key_right.get_size()[0]/2-text.get_size()[0]/2, self.key_right.get_size()[1]/2-text.get_size()[1]/2))

		self.key_stop = pygame.Surface(self.key_imj.get_size(), pygame.SRCALPHA, 32).convert_alpha()
		text = self.font.render("STOP", 0, (147, 147, 147))
		self.key_stop.blit(self.key_imj, (0, 0))
		self.key_stop.blit(text, (self.key_stop.get_size()[0]/2-text.get_size()[0]/2, self.key_stop.get_size()[1]/2-text.get_size()[1]/2))

		self.key_gaz = pygame.Surface(self.key_imj.get_size(), pygame.SRCALPHA, 32).convert_alpha()
		text = self.font.render("GAZ", 0, (147, 147, 147))
		self.key_gaz.blit(self.key_imj, (0, 0))
		self.key_gaz.blit(text, (self.key_gaz.get_size()[0]/2-text.get_size()[0]/2, self.key_gaz.get_size()[1]/2-text.get_size()[1]/2))

		self.key_left_rect = self.key_left.get_rect()
		self.key_right_rect = self.key_right.get_rect()
		self.key_stop_rect = self.key_stop.get_rect()
		self.key_gaz_rect = self.key_gaz.get_rect()

		self.key_left_rect.x = 6*self.mashtab
		self.key_left_rect.y = self.screen.get_size()[1]-self.key_left.get_size()[1]-6*self.mashtab

		self.key_right_rect.x = 6*self.mashtab*2+self.key_right.get_size()[0]
		self.key_right_rect.y = self.key_left_rect.y

		self.key_stop_rect.x = self.screen.get_size()[0]-self.key_stop.get_size()[0]-6*self.mashtab
		self.key_stop_rect.y = self.key_left_rect.y

		self.key_gaz_rect.x = self.screen.get_size()[0]-self.key_gaz.get_size()[0]*2-6*2*self.mashtab
		self.key_gaz_rect.y = self.key_left_rect.y

		self.keys_press = [0, 0, 0, 0] # left, right, stop, gaz
		self.keys_rects = [self.key_left_rect, self.key_right_rect, self.key_stop_rect, self.key_gaz_rect]

	def tick(self):
		if int(self.options.get(3)):
			for key_num in range(len(self.keys_press)):
				if len(self.tcursor.touch) > 0:
					for touch in self.tcursor.touch:
						pos = self.tcursor.touch[touch]
						rect = pygame.Surface((1, 1)).get_rect()
						rect.x = pos[0]
						rect.y = pos[1]

						collide = pygame.Rect.colliderect(rect, self.keys_rects[key_num])
						if collide:
							self.keys_press[key_num] = 1
							break
						else:
							self.keys_press[key_num] = 0
				else:
					self.keys_press[key_num] = 0

			self.screen.blit(self.key_left, (self.key_left_rect.x, self.key_left_rect.y))
			self.screen.blit(self.key_right, (self.key_right_rect.x, self.key_right_rect.y))
			self.screen.blit(self.key_stop, (self.key_stop_rect.x, self.key_stop_rect.y))
			self.screen.blit(self.key_gaz, (self.key_gaz_rect.x, self.key_gaz_rect.y))
			#print(self.keys_press)