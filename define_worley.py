from random import random
from Display.define_display import Display

class define_worley:
	def __init__(self):
		self.GridSize = 5
		self.CellSize = 100
		self.Noise = [[(10, 10, 10) for X in range(self.CellSize)] for Y in range(self.CellSize)]
		self.Diagram = [[(10, 10, 10) for X in range(self.CellSize)] for Y in range(self.CellSize)]
		self.DisplayDiagram = False
		self.DisplayGrid = False
		self.DisplayPoints = False
		self.create_grid()
		self.update_display()
	
	def create_grid(self):	
		self.Grid = []
		for Column in range(self.GridSize + 2):
			self.Grid.append([])
			for Row in range(self.GridSize + 2):
				self.Grid[Column].append((-1 + Row + random(), -1 + Column + random(), (int(random() * 255), int(random() * 255), int(random() * 255))))
		self.create_noise_diagram()

	def create_noise_diagram(self):
		for Y in range(self.CellSize):
			YPosition = Y / (self.CellSize / self.GridSize)
			for X in range(self.CellSize):
				XPosition = X / (self.CellSize / self.GridSize)
				LocalValues = []
				LocalColors = []
				for GridY in range(int(YPosition), int(YPosition) + 3):
					for GridX in range(int(XPosition), int(XPosition) + 3):
						LocalValues.append(((self.Grid[GridY][GridX][0] - XPosition) ** 2 + (self.Grid[GridY][GridX][1] - YPosition) ** 2) ** (1 / 2))
						LocalColors.append(self.Grid[GridY][GridX][2])
				self.Diagram[Y][X] = LocalColors[LocalValues.index(min(LocalValues))]
				if min(LocalValues) > 1:
					self.Noise[Y][X] = (255, 255, 255)
					continue
				self.Noise[Y][X] = (int(min(LocalValues) * 255), int(min(LocalValues) * 255), int(min(LocalValues) * 255))
	
	def update_display(self):
		self.DisplaySize = int(min(Display.WindowSize) / self.CellSize)
		if Display.WindowSize[0] > Display.WindowSize[1]:
			self.DisplayOffset = [int((max(Display.WindowSize) - min(Display.WindowSize)) / 2), 0]
		else:
			self.DisplayOffset = [0, int((max(Display.WindowSize) - min(Display.WindowSize)) / 2)]

WorleyNoise = define_worley()
