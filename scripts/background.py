# By OrangeDog Team, MG30.
# background.py - Анимированный бг(дорога) для бибик.

import pygame, os, sys

class background:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.surface = kwargs["surface"]

		self.speed = 0
		self.pause = 0

		self.bg1_rect = self.surface.get_rect()
		self.bg2_rect = self.surface.get_rect()
		self.bg_x = self.screen.get_size()[0]/2-self.surface.get_size()[0]/2
		self.bg1_rect.x = self.bg_x
		self.bg2_rect.x = self.bg_x
		self.screen_rect = self.screen.get_rect()
		self.set_pos_default()

	def set_pos_default(self):
		self.bg1_rect.y = self.surface.get_size()[1]-self.surface.get_size()[1]*2
		self.bg2_rect.y = 0

	def tick(self):
		if self.pause != 1:
			self.bg1_rect.y += self.speed
			self.bg2_rect.y += self.speed

			if (self.bg1_rect.y >= 0):
				self.set_pos_default()

		if pygame.Rect.colliderect(self.screen_rect, self.bg1_rect):
			self.screen.blit(self.surface, (self.bg1_rect.x, self.bg1_rect.y))

		if pygame.Rect.colliderect(self.screen_rect, self.bg2_rect):
			self.screen.blit(self.surface, (self.bg2_rect.x, self.bg2_rect.y))