# By OrangeDog Team, MG30.
# options.py - Настройки

import pygame, os, sys
from config import *
from scripts.txParser import *
from scripts.button import *
from scripts.tcursor import *

class options:
	def __init__(self, args):
		self.screen = args["screen"]
		self.go = args["go"]
		self.assets_import = args["assets_import"]
		self.path = args["path"]
		self.options = args["options"]

		self.tcursor = tcursor(screen=self.screen)
		self.options_temp = txParser()
		self.options_temp.read(self.path+"assets/values/options.txt")
		self.options_temp_2 = txParser()
		self.options_temp_2.read(self.path+"assets/values/options.txt")
		self.mashtab = int(self.options.get(0))
		self.undo_can = 0
		self.font_big = pygame.font.Font(self.path+font_path, 5*self.mashtab)
		self.font_small = pygame.font.Font(self.path+font_path, 3*self.mashtab)
		self.text_options = self.font_big.render("Настройки", 0, (255, 255, 255))
		self.menu_button = button(screen=self.screen, params=["Назад в меню", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.go_menu)
		self.undo_button = button(screen=self.screen, params=["Отменить действия", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.undo_all)
		self.save_button = button(screen=self.screen, params=["Сохранить", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.write_options)
		self.menu_button.rect.x = self.screen.get_size()[0]-self.menu_button.surface.get_size()[0]-self.mashtab*4
		self.menu_button.rect.y = self.screen.get_size()[1]-self.menu_button.surface.get_size()[1]-self.mashtab*4
		self.undo_button.rect.x = self.mashtab*4
		self.undo_button.rect.y = self.menu_button.rect.y
		self.save_button.rect.x = self.screen.get_size()[0]-self.save_button.surface.get_size()[0]-self.mashtab*4
		self.save_button.rect.y = self.menu_button.rect.y

		self.button_mashtab_minus = button(screen=self.screen, params=["-", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.minus_mashtab)
		self.button_mashtab_plus = button(screen=self.screen, params=["+", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.plus_mashtab)
		self.button_mashtab_minus.rect.x = self.screen.get_size()[0]-self.button_mashtab_minus.surface.get_size()[0]-self.mashtab*4
		self.button_mashtab_plus.rect.x = self.button_mashtab_minus.rect.x-self.mashtab*6
		self.button_fullscreen_change = button(screen=self.screen, params=["Вкл/Выкл", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.fullscreen_change)
		self.button_fullscreen_change.rect.x = self.screen.get_size()[0]-self.button_fullscreen_change.surface.get_size()[0]-self.mashtab*4
		self.button_fps_change = button(screen=self.screen, params=["Вкл/Выкл", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.fps_change)
		self.button_fps_change.rect.x = self.screen.get_size()[0]-self.button_fps_change.surface.get_size()[0]-self.mashtab*4
		self.button_touch_change = button(screen=self.screen, params=["Вкл/Выкл", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.touch_change)
		self.button_touch_change.rect.x = self.screen.get_size()[0]-self.button_touch_change.surface.get_size()[0]-self.mashtab*4
		self.button_touch_plus = button(screen=self.screen, params=["+", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.touch_plus)
		self.button_touch_minus = button(screen=self.screen, params=["-", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.touch_minus)
		self.button_touch_minus.rect.x = self.screen.get_size()[0]-self.button_mashtab_plus.surface.get_size()[0]-self.mashtab*4
		self.button_touch_plus.rect.x = self.button_mashtab_minus.rect.x-self.mashtab*6 
		self.button_thread_change = button(screen=self.screen, params=["Вкл/Выкл", (0, 0), 0], tcursor=self.tcursor, path=self.path, options=self.options, action=self.thread_change)
		self.button_thread_change.rect.x = self.screen.get_size()[0]-self.button_thread_change.surface.get_size()[0]-self.mashtab*4

	def truefalse_str(self, val):
		if val:
			return "Вкл"
		else:
			return "Выкл"

	def thread_change(self):
		self.undo_can = 1
		val = int(self.options_temp.get(5))
		if val:
			self.options_temp.set(5, 0)
			self.options.set(5, 0)
		else:
			self.options_temp.set(5, 1)
			self.options.set(5, 1)

	def touch_plus(self):
		self.undo_can = 1
		if int(self.options_temp.get(4)) < 10:
			self.options_temp.set(4, int(self.options_temp.get(4))+1)
			self.options.set(4, self.options_temp.get(4))

	def touch_minus(self):
		self.undo_can = 1
		if int(self.options_temp.get(4)) > 1:
			self.options_temp.set(4, int(self.options_temp.get(4))-1)
			self.options.set(4, self.options_temp.get(4))

	def touch_change(self):
		self.undo_can = 1
		val = int(self.options_temp.get(3))
		if val:
			self.options_temp.set(3, 0)
			self.options.set(3, 0)
		else:
			self.options_temp.set(3, 1)
			self.options.set(3, 1)

	def plus_mashtab(self):
		self.undo_can = 1
		if int(self.options_temp.get(0)) < 10:
			self.options_temp.set(0, int(self.options_temp.get(0))+1)

	def minus_mashtab(self):
		self.undo_can = 1
		if int(self.options_temp.get(0)) > 3:
			self.options_temp.set(0, int(self.options_temp.get(0))-1)

	def fullscreen_change(self):
		self.undo_can = 1
		val = int(self.options_temp.get(1))
		if val:
			self.options_temp.set(1, 0)
		else:
			self.options_temp.set(1, 1)

	def fps_change(self):
		self.undo_can = 1
		val = int(self.options_temp.get(2))
		if val:
			self.options_temp.set(2, 0)
			self.options.set(2, 0)
		else:
			self.options_temp.set(2, 1)
			self.options.set(2, 1)

	def go_menu(self):
		self.go(1)

	def undo_all(self):
		self.undo_can = 0
		self.options_temp.setAll(self.options_temp_2.getAll())

	def write_options(self):
		self.options_temp.update()
		self.undo_can = 0
		self.options_temp_2.setAll(self.options_temp.getAll())

	def tick(self):
		self.screen.fill((100, 100, 100))
		self.screen.blit(self.text_options, (self.screen.get_size()[0]/2-self.text_options.get_size()[0]/2, self.mashtab*5))
		if self.undo_can:
			self.undo_button.tick()
			self.save_button.tick()
		else:
			self.menu_button.tick()

		self.screen.blit(self.font_small.render("* Маштаб: "+str(self.options_temp.get(0)), 0, (255, 255, 255)), (self.mashtab*2, 20*self.mashtab))
		self.button_mashtab_minus.rect.y = 20*self.mashtab
		self.button_mashtab_plus.rect.y = 20*self.mashtab
		self.screen.blit(self.font_small.render("* Полноэкранный режим(ПК): "+self.truefalse_str(int(self.options_temp.get(1))), 0, (255, 255, 255)), (self.mashtab*2, 26*self.mashtab))
		self.button_fullscreen_change.rect.y = 26*self.mashtab
		self.screen.blit(self.font_small.render("Счётчик FPS: "+self.truefalse_str(int(self.options_temp.get(2))), 0, (255, 255, 255)), (self.mashtab*2, 32*self.mashtab))
		self.button_fps_change.rect.y=32*self.mashtab
		self.screen.blit(self.font_small.render("Сенсорное управление: "+self.truefalse_str(int(self.options_temp.get(3))), 0, (255, 255, 255)), (self.mashtab*2, 38*self.mashtab))
		self.button_touch_change.rect.y=38*self.mashtab
		self.screen.blit(self.font_small.render("Размер сенсорного управления: "+str(self.options_temp.get(4)), 0, (255, 255, 255)), (self.mashtab*2, 44*self.mashtab))
		self.button_touch_plus.rect.y = 44*self.mashtab
		self.button_touch_minus.rect.y = 44*self.mashtab
		self.screen.blit(self.font_small.render("Движение потока машин: "+self.truefalse_str(int(self.options_temp.get(5))), 0, (255, 255, 255)), (self.mashtab*2, 50*self.mashtab))
		self.button_thread_change.rect.y = 50*self.mashtab

		only_reset_text = self.font_small.render("* - Применяется после перезагрузки", 0, (255, 255, 255))
		self.screen.blit(only_reset_text, (self.undo_button.rect.x, self.undo_button.rect.y-only_reset_text.get_size()[1]-self.mashtab*2))

		self.button_mashtab_minus.tick()
		self.button_mashtab_plus.tick()
		self.button_fullscreen_change.tick()
		self.button_fps_change.tick()
		self.button_touch_change.tick()
		self.button_touch_plus.tick()
		self.button_touch_minus.tick()
		self.button_thread_change.tick()

		for event in pygame.event.get():
			self.tcursor.event(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()