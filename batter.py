#!/usr/bin/env python
#openCV version 3.2.0
#python version 3.0
#Cameron MacQuarrie 100770066
class Batter:
	def __init__(self, rawIn):
		self.name = rawIn[0]
		self.team = rawIn[1]
		self.fb = float(rawIn[2][:-1])/100
		self.gb = float(rawIn[3][:-1])/100
		self.iffb = float(rawIn[4][:-1])/100
		self.ld = float(rawIn[5][:-1])/100
		self.spd = float(rawIn[6])
		self.hard = float(rawIn[7][:-1])/100
		self.babip = float(rawIn[8])
		self.playerId = int(rawIn[9])
		self.trueIffb = self.fb*self.iffb
		self.trueFb = self.fb - (self.trueIffb)
	def addBBGBData(self, rawIn):
		if rawIn == 0:
			self.bbgbPull = 0
		else:
			self.bbgbPull = float(rawIn[45][:-1])/100
	def addShiftData(self, rawIn):
		if rawIn == 0:
			self.shiftBIP = 0
		else:
			self.shiftAB = int(rawIn[6])
			self.shiftSO = int(rawIn[16])
			self.shiftSF = int(rawIn[18])
			self.shiftBIP = self.shiftAB - self.shiftSO + self.shiftSF
	def addNoShiftData(self, rawIn):
		if rawIn == 0:
			self.noShiftBIP = 0
		else:
			self.noShiftAB = int(rawIn[6])
			self.noShiftSO = int(rawIn[16])
			self.noShiftSF = int(rawIn[18])
			self.noShiftBIP = self.noShiftAB - self.noShiftSO + self.noShiftSF
	def calculatexBABIP(self):
		if(self.noShiftBIP + self.shiftBIP) > 0:
			percentBallsInPlayShifted = self.shiftBIP / (self.noShiftBIP + self.shiftBIP)
		else:
			percentBallsInPlayShifted = 0 
		self.pullGBShift = self.gb * self.bbgbPull * percentBallsInPlayShifted
		self.xBABIP = 0.1911 + (self.ld*0.38) - (self.trueFb*0.1502) - (self.trueFb*0.1502) - (self.trueIffb*0.4173) + (self.hard*0.25502) + (self.spd*0.0049) - (self.pullGBShift*0.1492)
		print(self.name + "'s xBABIP: " + str(self.xBABIP))




