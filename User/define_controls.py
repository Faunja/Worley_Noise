import pygame
from time import time

class Define_Controls:
	def __init__(self):
		self.QuitGame = [pygame.K_ESCAPE]
		self.Fullscreen = [pygame.K_F11]
		self.ResetNoise = [pygame.K_r]
		
		self.PressedKeys = {}
	
	def check_key(self, Keybind):
		for Key in Keybind:
			if Key in self.PressedKeys:
				return Key
		return False

	def update_pressed_time(self, Keybind):
		self.PressedKeys[Keybind][0] = time()
		MinWaitTime = 10
		if len(self.PressedKeys[Keybind]) > 2:
			MinWaitTime = self.PressedKeys[Keybind][2]
		if self.PressedKeys[Keybind][1] < MinWaitTime:
			self.PressedKeys[Keybind][1] += 1

	def check_pressed_key(self, Keybinds):
		Keybind = check_key(Keybinds)
		if Keybind:
			if time.time() - self.PressedKeys[Keybind][0] > 1 / self.PressedKeys[Keybind][1]:
				update_pressed_time(Keybind)
				return True
		return False

Controls = Define_Controls()
