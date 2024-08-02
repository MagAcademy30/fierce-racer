# By OrangeDog Team, MG30.
# road.py - Класс дороги(Ни разу не BG!!!)

import pygame, os, sys, random

from config import *

class road:
	def __init__(self, **kwargs):
		self.screen = kwargs["screen"]
		self.background = kwargs["background"]
		self.player = kwargs["player"]
		self.assets_import = kwargs["assets_import"]
		self.options = kwargs["options"]
		textures = self.assets_import.get_texture()
		self.mashtab = int(self.options.get(0))
		self.gen_pos = (150 * self.mashtab, 550 * self.mashtab)
		self.pos = [self.background.bg_x+7.26*self.mashtab, self.background.bg_x+21.25*self.mashtab, self.background.bg_x+35.25*self.mashtab, self.background.bg_x+49.3*self.mashtab, self.background.bg_x+63.3*self.mashtab, self.background.bg_x+77.3*self.mashtab, self.background.bg_x+91.3*self.mashtab, self.background.bg_x+105.3*self.mashtab, self.background.bg_x+119*self.mashtab]
		self.gameover = 0
		self.pause = 0
		self.player.skip_x = self.background.bg_x
		self.cars = []
		self.cars_own_speed = []
		self.cars_speed = [0.5, 0.8, 1]
		self.debug_show_road = pygame.Surface((10*self.mashtab, 10*self.mashtab))
		self.debug_show_road.fill((255, 0, 0))
		self.screen_rect = self.screen.get_rect()
		self.cars_sprites = [
			textures["car"]["car_aqua"],
			textures["car"]["car_lime"],
			textures["car"]["car_taxi"],
			textures["car"]["car_white"],
			textures["bus"]["bus_aqua"],
			textures["bus"]["bus_grey"],
			textures["bus"]["bus_lime"],
			textures["gazzel"]["gazzel_aqua"],
			textures["gazzel"]["gazzel_lime"],
			textures["gazzel"]["gazzel_red"],
			textures["gazzel"]["gazzel_white"]
		]
		for i in range(len(self.pos)):
			self.cars.append(self.get_new_car(i))
			self.cars_own_speed.append(self.get_speed())

	def get_speed(self):
		if int(self.options.get(5)):
			return self.cars_speed[random.randint(0, len(self.cars_speed)-1)] * self.mashtab
		else:
			return 0

	def get_new_car(self, road_num):
		data = []
		y_pos = 0
		cocacola = self.cars_sprites[random.randint(0, len(self.cars_sprites)-1)]
		surface = pygame.Surface(cocacola.get_size(), pygame.SRCALPHA, 32)
		surface.blit(cocacola, (0, 0))
		surface = pygame.transform.rotate(surface, 180)
		rect = surface.get_rect()
		rect.x = self.pos[road_num]
		rect.y = random.randint(self.gen_pos[0], self.gen_pos[1]) * -1
		return [surface, rect]

	def tick(self):
		for road_num in range(len(self.cars)):
			car = self.cars[road_num]
			if car[1].y >= self.screen.get_size()[1]:
				self.cars[road_num] = self.get_new_car(road_num)
				self.cars_own_speed[road_num] = self.get_speed()
			else:
				if self.gameover == 0 and self.pause == 0: 
					car[1].y += self.background.speed + self.cars_own_speed[road_num]
				if pygame.Rect.colliderect(car[1], self.screen_rect):
					self.screen.blit(car[0], (car[1].x, car[1].y))
				if pygame.Rect.colliderect(car[1], self.player.rect) and disable_collision == 0:
					self.gameover = 1

		if debug:
			for i in self.pos:
				self.screen.blit(self.debug_show_road, (i, 0))