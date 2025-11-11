from random import random
from Display.define_display import Display

class define_worley:
	def __init__(self):
		self.GridSize = 5
		self.CellSize = 100
		self.Noise = [[10 for X in range(self.CellSize)] for Y in range(self.CellSize)]
		self.create_noise()
		self.update_display()

	def create_noise(self):	
		Grid = []
		for Column in range(self.GridSize + 2):
			Grid.append([])
			for Row in range(self.GridSize + 2):
				Grid[Column].append((-1 + Row + random(), -1 + Column + random()))

		for Y in range(self.CellSize):
			YPosition = Y / (self.CellSize / self.GridSize)
			for X in range(self.CellSize):
				XPosition = X / (self.CellSize / self.GridSize)
				LocalValues = []
				for GridY in range(int(YPosition), int(YPosition) + 3):
					for GridX in range(int(XPosition), int(XPosition) + 3):
						LocalValues.append(((Grid[GridY][GridX][0] - XPosition) ** 2 + (Grid[GridY][GridX][1] - YPosition) ** 2) ** (1 / 2))
				if min(LocalValues) > 1:
					self.Noise[Y][X] = 255
					continue
				self.Noise[Y][X] = int(min(LocalValues) * 255)
	
	def update_display(self):
		self.DisplaySize = int(min(Display.WindowSize) / self.CellSize)
		if Display.WindowSize[0] > Display.WindowSize[1]:
			self.DisplayOffset = [int((max(Display.WindowSize) - min(Display.WindowSize)) / 2), 0]
		else:
			self.DisplayOffset = [0, int((max(Display.WindowSize) - min(Display.WindowSize)) / 2)]

WorleyNoise = define_worley()
