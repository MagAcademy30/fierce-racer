# By OrangeDog Team, MG30
# player.py - БИБИ))

import pygame, os, sys

from config import *

class player:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.skin = kwargs["skin"]
		self.background = kwargs["background"]
		self.joystick_controls = kwargs["joystick_controls"]
		self.options = kwargs["options"]
		self.sensor_keys = kwargs["sensor_keys"]
		self.sound = kwargs["sound"]
		self.score = 0
		self.mashtab = int(self.options.get(0))
		self.surface = pygame.Surface(self.skin.get_size(), pygame.SRCALPHA, 32)
		self.surface.blit(self.skin, (0, 0))
		self.rect = self.surface.get_rect()
		self.rect.x = self.screen.get_size()[0]/2-self.surface.get_size()[0]/2
		self.rect.y = player_pos[1]*self.mashtab
		self.skip_x = 0
		self.pause = 0
		self.move_playonce = 1

		self.speed = 0
		self.speed_max = 20
		self.speed_add = 0.02
		self.speed_add_temp = self.speed_add
		self.speed_add_remove = 0.001
		self.sound.play("gfx", "car_engine", -1)

	def speed_up(self):
		if self.speed <= self.speed_max:
			self.speed += self.speed_add * self.mashtab
			if self.move_playonce:
				self.sound.play("gfx", "car_move", -1)
				self.move_playonce = 0

	def speed_down(self):
		if self.speed >= 0:
			self.speed -= 0.003 * self.mashtab
		else:
			self.sound.stop("gfx", "car_move")
			self.move_playonce = 1

	def speed_stop(self):
		if self.speed >= 0:
			self.speed -= 0.03 * self.mashtab

	def tick(self):
		self.score += round(self.speed)
		if self.pause == 0:
			# Газ
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE] or self.sensor_keys.keys_press[3] or self.joystick_controls.key_pressed[2]:
				self.speed_up()
			else:
				self.speed_down()
			
			if keys[pygame.K_LSHIFT] or self.sensor_keys.keys_press[2] or self.joystick_controls.key_pressed[3]:
				self.speed_stop()

			if keys[pygame.K_LEFT] or keys[pygame.K_a] or self.sensor_keys.keys_press[0] or self.joystick_controls.key_pressed[0]:
				if self.rect.x > self.skip_x:
					self.rect.x = round(self.rect.x - 1 * self.mashtab)
				else:
					self.rect.x = self.skip_x

			if keys[pygame.K_RIGHT] or keys[pygame.K_d] or self.sensor_keys.keys_press[1] or self.joystick_controls.key_pressed[1]:
				if self.rect.x < self.screen.get_size()[0]-self.surface.get_size()[0]-self.skip_x:
					self.rect.x = round(self.rect.x + 1 * self.mashtab)
				else:
					self.rect.x = self.screen.get_size()[0]-self.surface.get_size()[0]-self.skip_x

			if self.speed <= -1:
				self.speed = 0

			self.background.speed = round(self.speed)

		self.screen.blit(self.surface, (self.rect.x, self.rect.y))