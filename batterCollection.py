#!/usr/bin/env python
#openCV version 3.2.0
#python version 3.0
#Cameron MacQuarrie 100770066
import batter
import time
import datetime
import csv
from tkinter.filedialog import askopenfilename

class BatterCollection:
	def __init__(self):
		self.batters = []
		print('Open BASE batter data set...')
		
		with open(askopenfilename()) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			li = list(readCSV)
			del li[0]
			for bat in li:
				self.batters.append(batter.Batter(bat))
		self.batters = sorted(self.batters, key=lambda bat: bat.playerId)
		print('Open SHIFT batter data set...')
		with open(askopenfilename()) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			li = list(readCSV)
			del li[0]
			self.addShiftData(li)
		print('Open NO SHIFT batter data set...')
		with open(askopenfilename()) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			li = list(readCSV)
			del li[0]
			self.addNoShiftData(li)
		print('Open BBGB batter data set...')
		with open(askopenfilename()) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			li = list(readCSV)
			del li[0]
			self.addBBGBData(li)
		self.lastUpdate = time.time()
		for bat in self.batters:
			bat.calculatexBABIP()
	def lastUpdateStr(self):
		return datetime.datetime.fromtimestamp(self.lastUpdate).strftime('%b %d, %Y')
	def size(self):
		return len(self.batters)
	def addBBGBData(self, rawIn):
		curIndex = 0
		for bat in rawIn:
			batId = int(bat[2])
			noMatch = True
			while(noMatch):
				#if the next batter in line matches, add their bbgb data
				if (batId == self.batters[curIndex].playerId):
					self.batters[curIndex].addBBGBData(bat)
					curIndex += 1
					noMatch = False
				#otherwise set a flag that bbgb data doesnt exist for that index
				elif (batId >= self.batters[curIndex].playerId):
					self.batters[curIndex].addBBGBData(0)
					curIndex += 1
				#If the next playerId is somehow larger than the current one, just skip it
				else:
					noMatch = False
	def addShiftData(self, rawIn):
		curIndex = 0
		for bat in rawIn:
			batId = int(bat[2])
			noMatch = True
			while(noMatch):
				#if the next batter in line matches, add their bbgb data
				if (batId == self.batters[curIndex].playerId):
					self.batters[curIndex].addShiftData(bat)
					curIndex += 1
					noMatch = False
				#otherwise set a flag that bbgb data doesnt exist for that index
				elif (batId >= self.batters[curIndex].playerId):
					self.batters[curIndex].addShiftData(0)
					curIndex += 1
				#If the next playerId is somehow larger than the current one, just skip it
				else:
					noMatch = False
	def addNoShiftData(self, rawIn):
		curIndex = 0
		for bat in rawIn:
			batId = int(bat[2])
			noMatch = True
			while(noMatch):
				#if the next batter in line matches, add their bbgb data
				if (batId == self.batters[curIndex].playerId):
					self.batters[curIndex].addNoShiftData(bat)
					curIndex += 1
					noMatch = False
				#otherwise set a flag that bbgb data doesnt exist for that index
				elif (batId >= self.batters[curIndex].playerId):
					self.batters[curIndex].addNoShiftData(0)
					curIndex += 1
				#If the next playerId is somehow larger than the current one, just skip it
				else:
					noMatch = False
	def exportCSV(self, filename):
		with open(filename, 'w') as csvfile:
			writeCSV = csv.writer(csvfile, delimiter=',')
			writeCSV.writerow(['Name', 'xBABIP', 'BABIP', 'LD%', 'TrueFB%', 'TrueIFFB%', 'Hard%', 'Spd', 'Pull GB While Shifted'])
			for bat in self.batters:
				writeCSV.writerow([bat.name, str(bat.xBABIP), str(bat.babip), str(bat.ld), str(bat.trueFb), str(bat.trueIffb), str(bat.hard), str(bat.spd), str(bat.pullGBShift)])


