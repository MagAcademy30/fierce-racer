# By OrangeDog Team, MG30.
# tcursor.py - Класс который отвечает за ввод мыши и тачскрина.

import pygame, os, sys
from random import randint

class tcursor:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.cursor = [[0, 0], 0]
		self.touch = {}
		self.screensize = self.screen.get_size()

	def event(self, event):
		# Если мышь двигается(или нажимается), то пишем её позицию в список.
		if event.type == pygame.MOUSEMOTION:
			self.cursor[0] = event.pos

		# Нажатие мыши
		if event.type == pygame.MOUSEBUTTONUP:
			self.cursor[0] = event.pos
			self.cursor[1] = 0
		elif event.type == pygame.MOUSEBUTTONDOWN:
			self.cursor[0] = event.pos
			self.cursor[1] = 1

		# Тач
		if event.type == pygame.FINGERMOTION or event.type == pygame.FINGERDOWN:
			pos = (round(self.screensize[0]*event.x), round(self.screensize[1]*event.y))
			self.touch[event.finger_id] = pos

		elif event.type == pygame.FINGERUP:
			try:
				self.touch.pop(event.finger_id)
			except KeyError:
				pass