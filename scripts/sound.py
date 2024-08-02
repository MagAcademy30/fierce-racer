# By OrangeDog Team, MG30
# sound.py - класс для работы со звуком

import pygame, os, sys
from config import *

class sound:
	def __init__(self, **kwargs):
		self.sounds = kwargs["sounds"]
		self.is_mute = 0

	def mute(self):
		self.is_mute = 1
		self.stop_all()

	def unmute(self):
		self.is_mute = 0

	def stop_all(self):
		for a in self.sounds:
			for b in self.sounds[a]:
				self.sounds[a][b].stop()

	def stop(self, dir, sound):
		self.sounds[dir][sound].stop()

	def play(self, dir, sound, loops):
		if self.is_mute == 0:
			self.sounds[dir][sound].play(loops=loops)