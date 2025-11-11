from pygame import time

class Define_User:
	def __init__(self):
		self.FPS = 60
		self.AffectiveFPS = self.FPS
		self.Clock = time.Clock()
		
		self.Playing = True

User = Define_User()

