# By OrangeDog Team, MG30.
# main.py содержит основной код который работает с классами и меню

import pygame, os, sys
from config import *
from scripts.txParser import *
from scripts.is_android import *
from scripts.assets_import import *
from scripts.fps_counter import *
from menus.intro import *
from menus.main_menu import *
from menus.testRoom import *
from menus.test_keys import *
from menus.game import *
from menus.options import *

pygame.init()
pygame.joystick.init()
pygame.mixer.init(channels=mixer_channels)

class Game:
	def __init__(self):
		self.path = os.path.abspath(".")+'/'
		self.options = txParser()
		self.options.read(self.path+"assets/values/options.txt")
		self.android = is_android()
		res = (screensize[0]*int(self.options.get(0)), screensize[1]*int(self.options.get(0)))
		if self.android:
			self.screen = pygame.display.set_mode(res, pygame.FULLSCREEN | pygame.SCALED)
		elif int(self.options.get(1)):
			self.screen = pygame.display.set_mode(res, pygame.FULLSCREEN | pygame.SCALED)
		else: 
			self.screen = pygame.display.set_mode(res)
		self.clock = pygame.time.Clock()
		self.assets_import = assets_import(self.options, self.path)
		self.fps_counter = fps_counter(screen=self.screen, options=self.options, clock=self.clock, path=self.path)

		pygame.display.set_caption("Лютый Гонщик "+version)

		self.room_args = {
			"screen": self.screen,
			"android": self.android,
			"options": self.options,
			"assets_import": self.assets_import,
			"go": self.go,
			"go_previos": self.go_previos,
			"path": self.path
		}
		self.rooms = [intro, main_menu, test_keys, game, options]
		self.room = 0
		self.room_previos = self.room

		self.new_room_go = 0
		while 1:
			room = self.rooms[self.room](self.room_args)
			while self.new_room_go != 1:
				room.tick()
				if int(self.options.get(2)):
					self.fps_counter.tick()
				pygame.display.flip()
				self.clock.tick(fps)
			self.new_room_go = 0

	def go(self, num):
		self.room_previos = self.room
		self.room = num
		self.new_room_go = 1

	def go_previos(self):
		self.room = self.room_previos
		self.new_room_go = 1

	def exit(self):
		pygame.quit()
		sys.exit()

if __name__ == "__main__":
	game = Game()