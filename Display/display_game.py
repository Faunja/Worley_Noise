import pygame
from copy import deepcopy
from time import time
from define_worley import WorleyNoise
from User.define_cursor import Cursor
from User.define_user import User
from Display.define_display import Display

def draw_polygon_alpha(Color, Points):
	xPoints, yPoints = zip(*Points)
	MinimumX, MinimumY, MaximumX, MaximumY = min(xPoints), min(yPoints), max(xPoints), max(yPoints)
	AlphaRect = pygame.Rect(MinimumX, MinimumY, MaximumX - MinimumX, MaximumY - MinimumY)
	AlphaSurface = pygame.Surface(AlphaRect.size, pygame.SRCALPHA)
	pygame.draw.polygon(AlphaSurface, Color, [(X - MinimumX, Y - MinimumY) for X, Y in Points])
	Display.Window.blit(AlphaSurface, AlphaRect)

def draw_text(Text, Position, Orientation = [0, 0], Font = Display.Font, Color = (255, 255, 255)):
	Text = Font.render(Text, True, Color)
	TextWidth, TextHeight = Text.get_size()
	Orientation = [TextWidth * (Orientation[0] - .5), TextHeight * (Orientation[1] - .5)]
	Display.Window.blit(Text, (Position[0] + Orientation[0], Position[1] + Orientation[1]))
	return TextWidth, TextHeight

def draw_click():
	for Position in deepcopy(Cursor.ClickPositions):
		Age = (Cursor.ClickAlphaTimer - time() + Cursor.ClickPositions[Position]) / Cursor.ClickAlphaTimer
		if Age <= 0:
			del Cursor.ClickPositions[Position]
			continue
		X, Y = Position
		Radius = Cursor.Radius + int(Cursor.Radius * (Cursor.ClickSize * (1 + (Cursor.ClickGrowthSize - 1) * (1 - Age)) - 1))
		draw_polygon_alpha((255, 255, 255, 255 * Age), ((X, Y - Radius), (X + Radius, Y), (X, Y + Radius), (X - Radius, Y)))

def draw_cursor():
	draw_click()
	X, Y = Cursor.Position
	Radius = Cursor.Radius + int(Cursor.Radius * (Cursor.ClickSize - 1)) * int(Cursor.LeftClick or Cursor.RightClick)
	AlphaOffset = int(255 * (time() - Cursor.TimeSinceAction - Cursor.StartAlphaTimer) / (Cursor.EndAlphaTimer - Cursor.StartAlphaTimer))
	AlphaStage = 255 - AlphaOffset * int(time() - Cursor.TimeSinceAction > Cursor.StartAlphaTimer)
	Alpha = AlphaStage * int(time() - Cursor.TimeSinceAction < Cursor.EndAlphaTimer)
	draw_polygon_alpha((255, 255, 255, Alpha), ((X, Y - Radius), (X + Radius, Y), (X, Y + Radius), (X - Radius, Y)))
	if not Cursor.LeftClick or not Cursor.RightClick:
		Radius = int(Radius * (3 / 4))
		draw_polygon_alpha((0, 0, 0, Alpha), ((X, Y - Radius), (X + Radius * int(not Cursor.RightClick), Y), (X, Y + Radius), (X - Radius * int(not Cursor.LeftClick), Y)))

def display_noise():
	Noise = WorleyNoise.Noise
	Diagram = WorleyNoise.Diagram
	for Column in range(WorleyNoise.CellSize):
		YPosition = Column * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[1]
		for Row in range(WorleyNoise.CellSize):
			XPosition = Row * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[0]
			if WorleyNoise.DisplayDiagram:
				pygame.draw.rect(Display.Window, Diagram[Column][Row], (XPosition, YPosition, WorleyNoise.DisplaySize, WorleyNoise.DisplaySize))
				continue
			pygame.draw.rect(Display.Window, Noise[Column][Row], (XPosition, YPosition, WorleyNoise.DisplaySize, WorleyNoise.DisplaySize))

def display_points():
	Points = WorleyNoise.Grid
	for Column in range(1, WorleyNoise.GridSize + 1):
		for Row in range(1, WorleyNoise.GridSize + 1):
			XPosition = Points[Column][Row][0] * int(WorleyNoise.CellSize / WorleyNoise.GridSize) * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[0]
			YPosition = Points[Column][Row][1] * int(WorleyNoise.CellSize / WorleyNoise.GridSize) * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[1]
			pygame.draw.circle(Display.Window, (0, 0, 0), (XPosition, YPosition), 7)
			pygame.draw.circle(Display.Window, Points[Column][Row][2], (XPosition, YPosition), 5)
	
def display_grid():
	for Column in range(1, WorleyNoise.GridSize):
		YPosition = Column * int(WorleyNoise.CellSize / WorleyNoise.GridSize) * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[1]
		pygame.draw.line(Display.Window, (0, 0, 0), (WorleyNoise.DisplayOffset[0], YPosition), (WorleyNoise.DisplayOffset[0] + WorleyNoise.CellSize * WorleyNoise.DisplaySize, YPosition), 3)
	for Row in range(1, WorleyNoise.GridSize):
		XPosition = Row * int(WorleyNoise.CellSize / WorleyNoise.GridSize) * WorleyNoise.DisplaySize + WorleyNoise.DisplayOffset[0]
		pygame.draw.line(Display.Window, (0, 0, 0), (XPosition, WorleyNoise.DisplayOffset[1]), (XPosition, WorleyNoise.DisplayOffset[1] + WorleyNoise.CellSize * WorleyNoise.DisplaySize), 3)

def display_game():
	Display.Window.fill((0, 0, 0))
	display_noise()
	if WorleyNoise.DisplayGrid:
		display_grid()
	if WorleyNoise.DisplayPoints:
		display_points()
	draw_text(str(int(User.AffectiveFPS)), (0, 0), (.5, .5))
	draw_cursor()
	
