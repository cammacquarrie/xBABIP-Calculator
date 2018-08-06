#!/usr/bin/env python
#openCV version 3.2.0
#python version 3.0
#Cameron MacQuarrie 100770066

from tkinter.filedialog import askopenfilename
import pickle
import batterCollection

print('Welcome.')
noData = True
while(noData):
	command = input('(1) Load or (2) New: ')
	if command == '1' or command.lower() == 'load':
		filepath = askopenfilename()
		with open(filepath, 'rb') as input:
			batters = pickle.load(input)
			print('Last update: ' + batters.lastUpdateStr())
			print(filepath)
		noData = False
	elif command == '2' or command.lower() == 'new':
		batters = batterCollection.BatterCollection()
		noData = False
	else:
		print('invalid input')
		
	#outfile = open('saved_data.pk1', 'wb')
	#pickle.dump(batters, outfile)
	#outfile.close()
	filename = batters.lastUpdateStr() + ".csv"
	batters.exportCSV(filename)
	print(batters.size())