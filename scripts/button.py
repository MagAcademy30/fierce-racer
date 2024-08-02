# By OrangeDog Team, MG30
# button.py - Класс кнопки.

import pygame, os, sys, random
from config import *

class button:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.params = kwargs["params"] # ["Текст", (x, y), Тип] - 0 - Одно касание, 1 - Зажатие(как нажал, без отпускания активируется.)
		self.tcursor = kwargs["tcursor"]
		self.path = kwargs["path"]
		self.options = kwargs["options"]
		self.action = kwargs["action"]

		self.state = 0
		self.already_pressed = 0
		self.collide = 0
		self.old_mouse = self.tcursor.cursor
		mashtab = int(self.options.get(0))
		self.font_obj = pygame.font.Font(self.path+font_path, 3*mashtab)
		self.font_surface = self.font_obj.render(self.params[0], 0, button_colors[2])
		self.surface = pygame.Surface((mashtab*2+self.font_surface.get_size()[0], mashtab*2+self.font_surface.get_size()[1]))
		self.update_state()
		self.rect = self.surface.get_rect()
		self.rect.x = self.params[1][0]
		self.rect.y = self.params[1][1]

	def update_state(self):
		self.surface.fill(button_colors[self.state])
		self.surface.blit(self.font_surface, (self.surface.get_size()[0]/2-self.font_surface.get_size()[0]/2, self.surface.get_size()[1]/2-self.font_surface.get_size()[1]/2))

	def tick(self):
		pressed = 0
		rect = pygame.Surface((1, 1)).get_rect()

		if len(self.tcursor.touch) > 0:
			has = 0
			for f_id in self.tcursor.touch:
				pos = self.tcursor.touch[f_id]		
				rect.x = pos[0]
				rect.y = pos[1]

				if pygame.Rect.colliderect(self.rect, rect):
					self.collide = pygame.Rect.colliderect(self.rect, rect)
					pressed = 1
					break
				else:
					pressed = 0
		else:
			pressed = self.tcursor.cursor[1]
			rect.x = self.tcursor.cursor[0][0]
			rect.y = self.tcursor.cursor[0][1]
			self.collide = pygame.Rect.colliderect(self.rect, rect)

		if self.collide:
			self.state = 1
			if self.params[2] == 0:
				if pressed:
					self.already_pressed = 1
				else:
					if self.already_pressed:
						self.action()
						self.already_pressed = 0
			elif self.params[2] == 1:
				if pressed:
					self.state = 1
					self.action()
		else:
			self.state = 0
			self.already_pressed = 0

		self.update_state()
		self.screen.blit(self.surface, (self.rect.x, self.rect.y))