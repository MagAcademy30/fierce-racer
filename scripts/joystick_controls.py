# By OrangeDog Team, MG30.
# joystick_controls.py - Класс для управление игроком через джостик.

import pygame, os, sys

class joystick_controls:
	def __init__(self):
		self.keymap = [13, 14, 10, 9] #left, right. speed, stop
		self.key_pressed = [0, 0, 0, 0]

		self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

	def tick(self):
		for joystick in self.joysticks:
			buttons_num = joystick.get_numbuttons()
			for i in range(buttons_num):
				button_state = joystick.get_button(i)
				for key_num in range(len(self.keymap)):
					if self.keymap[key_num] == i:
						self.key_pressed[key_num] = button_state