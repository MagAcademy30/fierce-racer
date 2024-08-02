# By OrangeDog Team, MG30
# game.py - Игра

import pygame, os, sys

from config import *
from scripts.background import *
from scripts.sensor_keys import *
from scripts.joystick_controls import *
from scripts.tcursor import *
from scripts.player import *
from scripts.road import *
from scripts.button import *
from scripts.sound import *
from scripts.speedometer import *

class game:
	def __init__(self, args):
		self.screen = args["screen"]
		self.go = args["go"]
		self.go_previos = args["go_previos"]
		self.assets_import = args["assets_import"]
		self.path = args["path"]
		self.options = args["options"]
		self.mashtab = int(self.options.get(0))

		self.playgameover = 1
		self.pause = 0
		self.sound = sound(sounds=self.assets_import.get_sound())
		self.bg_black = pygame.Surface(self.screen.get_size())
		self.bg_black.set_alpha(100)
		self.joystick_controls = joystick_controls()
		self.tcursor = tcursor(screen=self.screen)
		self.background = background(screen=self.screen, surface=self.assets_import.get_texture()["bg"]["bg_default"])
		self.sensor_keys = sensor_keys(screen=self.screen, assets_import=self.assets_import, path=self.path, options=self.options, tcursor=self.tcursor)
		self.player = player(screen=self.screen, skin=self.assets_import.get_texture()["skin"]["skin_sportlime"], background=self.background, options=self.options, sensor_keys=self.sensor_keys, joystick_controls=self.joystick_controls, sound=self.sound)
		self.road = road(screen=self.screen, background=self.background, player=self.player, assets_import=self.assets_import, options=self.options)
		self.font_gameover = pygame.font.Font(self.path+font_path, 10*self.mashtab)
		self.font_pause = pygame.font.Font(self.path+font_path, 5*self.mashtab)
		self.font_score = pygame.font.Font(self.path+font_path, 3*self.mashtab)
		self.text_pause = self.font_pause.render("Pause", 0, (255, 255, 255))
		self.text_gameover = self.font_gameover.render("Game Over!", 0, (255, 255, 255))
		self.button_new_game = button(screen=self.screen, params=["Рестарт", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.new_game)
		self.button_back_to_menu = button(screen=self.screen, params=["В Главное меню", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.back_to_menu)
		self.button_pause = button(screen=self.screen, params=["Пауза", (0, self.mashtab), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_to_pause)
		self.button_pause_go_game = button(screen=self.screen, params=["Назад", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_to_game)
		self.button_pause_go_menu = button(screen=self.screen, params=["В Главное меню", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_to_menu)
		self.button_back_to_menu.rect.x = self.screen.get_size()[0]-self.button_back_to_menu.surface.get_size()[0]-5*self.mashtab
		self.button_back_to_menu.rect.y = self.screen.get_size()[1]/2-self.button_back_to_menu.surface.get_size()[1]/4-5*self.mashtab
		self.button_new_game.rect.x = self.screen.get_size()[0]-self.button_new_game.surface.get_size()[0]-self.mashtab*4
		self.button_new_game.rect.y = self.screen.get_size()[1]/2-self.button_new_game.surface.get_size()[1]/2
		self.button_pause.rect.x = self.screen.get_size()[0]/2-self.button_pause.surface.get_size()[0]/2
		self.speedometer = speedometer(screen=self.screen, player=self.player, path=self.path, options=self.options)
		self.button_pause_go_menu.rect.x = self.screen.get_size()[0]/2-self.button_pause_go_menu.surface.get_size()[0]/2
		self.button_pause_go_game.rect.x = self.screen.get_size()[0]/2-self.button_pause_go_game.surface.get_size()[0]/2
		self.button_pause_go_menu.rect.y = self.screen.get_size()[1]-self.button_pause_go_menu.surface.get_size()[1]-self.mashtab*5
		self.button_pause_go_game.rect.y = self.screen.get_size()[1]-self.button_pause_go_game.surface.get_size()[1]-self.mashtab*11

		self.sound.mute()

	def go_to_menu(self):
		self.go(1)

	def go_to_game(self):
		self.pause = 0
		self.player.pause = 0
		self.road.pause = 0

	def go_to_pause(self):
		self.pause = 1
		self.player.pause = 1
		self.road.pause = 1
		self.background.speed = 0

	def new_game(self):
		self.go(3)

	def back_to_menu(self):
		self.go(1)

	def tick(self):
		self.screen.fill((0, 0, 0))
		self.background.tick()
		self.joystick_controls.tick()
		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE]:
			self.go_to_pause()

		self.player.tick()
		self.road.tick()
		self.speedometer.tick()
		#score_text = self.font_score.render("Очки: "+str(self.player.score), 0, (255, 255, 255))
		#self.screen.blit(score_text, (0, 0))
		if self.pause == 0 and int(self.options.get(3)) and self.road.gameover == 0:
			self.button_pause.tick()
			self.sensor_keys.tick()

		if self.road.gameover:
			if self.playgameover:
				self.sound.stop_all()
				self.sound.play("gfx", "car_crash", 0)
				self.playgameover = 0
			self.background.speed = 0
			self.player.pause = 1
			self.screen.blit(self.bg_black, (0, 0))
			self.screen.blit(self.text_gameover, (10*self.mashtab, self.screen.get_size()[1]/2-self.text_gameover.get_size()[1]/2))
			self.button_new_game.tick()
			#self.button_back_to_menu.tick()
		elif self.pause:
			self.screen.blit(self.bg_black, (0, 0))
			self.screen.blit(self.text_pause, (self.screen.get_size()[0]/2-self.text_pause.get_size()[0]/2, self.mashtab*5))
			self.button_pause_go_game.tick()
			self.button_pause_go_menu.tick()

		for event in pygame.event.get():
			self.tcursor.event(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
