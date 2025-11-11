from copy import deepcopy
import pygame

class Define_Display:
	def __init__(self):
		self.Fullscreen = False
		Screen = pygame.display.get_desktop_sizes()
		self.ScreenSize = list(pygame.display.get_desktop_sizes())[0]
		self.WindowSize = [int(self.ScreenSize[0] * (4 / 5)), int(self.ScreenSize[1] * (4 / 5))]

		self.update_display()

	def update_display(self, Width = None, Height = None):
		if Width and Height:
			self.WindowSize = [Width, Height]
		if self.Fullscreen == False:
			self.Window = pygame.display.set_mode((self.WindowSize[0], self.WindowSize[1]))
		else:
			self.Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.Font = pygame.font.SysFont("lexend", int(min(self.WindowSize[0], self.WindowSize[1]) / 16))
	
	def toggle_fullscreen(self):
		self.Fullscreen = not self.Fullscreen
		if self.Fullscreen:
			self.OldWindowSize = deepcopy(self.WindowSize)
			self.update_display(self.ScreenSize[0], self.ScreenSize[1])
		else:
			self.update_display(self.OldWindowSize[0], self.OldWindowSize[1])

Display = Define_Display()
