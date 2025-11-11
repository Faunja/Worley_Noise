from copy import deepcopy
from Display.define_display import Display
from pygame import draw, mouse
from time import time

class define_cursor:
	def __init__(self):
		mouse.set_visible(False)
		self.Position = mouse.get_pos()
		self.Radius = 6
		self.LeftClick = False
		self.RightClick = False
		
		self.TimeSinceAction = time()
		self.StartAlphaTimer = 4
		self.EndAlphaTimer = 6
		
		self.ClickPositions = {}
		self.ClickSize = 1.2
		self.ClickGrowthSize = int(self.ClickSize * 2.5)
		self.ClickAlphaTimer = .2
	
	def click(self, Click):
		if Click == 1:
			self.LeftClick = not self.LeftClick
			if not self.LeftClick:
				return
		elif Click == 3:
			self.RightClick = not self.RightClick
			if not self.RightClick:
				return
		else:
			return
		self.ClickPositions[deepcopy(self.Position)] = time()
	
	def update_cursor(self):
		PreviousPosition = deepcopy(self.Position)
		self.Position = mouse.get_pos()
		if PreviousPosition != self.Position or self.LeftClick or self.RightClick:
			self.TimeSinceAction = time()

Cursor = define_cursor()
