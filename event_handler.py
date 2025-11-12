import pygame
from define_worley import WorleyNoise
from User.define_controls import Controls
from User.define_cursor import Cursor
from User.define_user import User
from Display.define_display import Display

def update_key_down(Key):
	if Key in Controls.QuitGame:
		User.Playing = False
	if Key in Controls.Fullscreen:
		Display.toggle_fullscreen()
		WorleyNoise.DisplaySize = int(min(Display.WindowSize) / WorleyNoise.CellSize)
		if Display.WindowSize[0] > Display.WindowSize[1]:
			WorleyNoise.DisplayOffset = [int((max(Display.WindowSize) - min(Display.WindowSize)) / 2), 0]
		else:
			WorleyNoise.DisplayOffset = [0, int((max(Display.WindowSize) - min(Display.WindowSize)) / 2)]
	if Key in Controls.ResetGrid:
		WorleyNoise.create_grid()
	if Key in Controls.SwitchDisplay:
		WorleyNoise.DisplayDiagram = not WorleyNoise.DisplayDiagram
	if Key in Controls.ToggleGrid:
		WorleyNoise.DisplayGrid = not WorleyNoise.DisplayGrid
	if Key in Controls.TogglePoints:
		WorleyNoise.DisplayPoints = not WorleyNoise.DisplayPoints

def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			Cursor.click(event.button)
		if event.type == pygame.MOUSEBUTTONUP:
			Cursor.click(event.button)

		if event.type == pygame.KEYDOWN:
			update_key_down(event.key)

		if event.type == pygame.QUIT:
			User.Playing = False
	
	Cursor.update_cursor()
