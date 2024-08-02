# By OrangeDog Team, MG30
# fps_counter.py - Счётчик FPS

import pygame, os, sys
from config import *

class fps_counter:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.options = kwargs["options"]
		self.clock = kwargs["clock"]
		self.path = kwargs["path"]
		self.mashtab = int(self.options.get(0))
		self.font = pygame.font.Font(self.path+font_path, 3*self.mashtab)

	def tick(self):
		self.screen.blit(self.font.render(str(int(self.clock.get_fps())), 0, (255, 0, 0)), (0, 0))