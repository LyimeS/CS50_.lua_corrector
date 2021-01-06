#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
import sys

#########################################################
# FORMAT Title (just an aesthetic detail)
#########################################################
def title (txt):
	print("-" * len(txt), end="-- \n")
	print("\033[44m " + txt, end=" \033[m \n")
	print("-" * len(txt), end="--\n")

#########################################################
# File correction
#########################################################
#=============================
# dictionary of terms to be corrected
#=============================
terms = {
	"getPixelScale": "getDPIScale",
	"graphics.clear(40, 45, 52, 255)": "graphics.clear(40/255, 45/255, 52/255, 1)",  # pong
	"graphics.clear(108, 140, 255, 255)": "graphics.clear(108/255, 140/255, 255/255, 255/255)", # mario-demo
	"audio.newSource('music/overworld.mp3')": "audio.newSource('music/overworld.mp3', 'static')", # mario-demo
	"audio.newSource('sounds/paddle_hit.wav')" : "audio.newSource('sounds/paddle_hit.wav', 'static')", #Breakout
	"audio.newSource('sounds/score.wav')" : "audio.newSource('sounds/score.wav', 'static')", #Breakout
	"audio.newSource('sounds/wall_hit.wav')" : "audio.newSource('sounds/wall_hit.wav', 'static')", #Breakout
	"audio.newSource('sounds/confirm.wav')" : "audio.newSource('sounds/confirm.wav', 'static')", #Breakout
	"audio.newSource('sounds/select.wav')" : "audio.newSource('sounds/select.wav', 'static')", #Breakout
	"audio.newSource('sounds/no-select.wav')" : "audio.newSource('sounds/no-select.wav', 'static')", #Breakout
	"audio.newSource('sounds/brick-hit-1.wav')" : "audio.newSource('sounds/brick-hit-1.wav', 'static')", #Breakout
	"audio.newSource('sounds/brick-hit-2.wav')" : "audio.newSource('sounds/brick-hit-2.wav', 'static')", #Breakout
	"audio.newSource('sounds/hurt.wav')" : "audio.newSource('sounds/hurt.wav', 'static')", #Breakout
	"audio.newSource('sounds/victory.wav')" : "audio.newSource('sounds/victory.wav', 'static')", #Breakout
	"audio.newSource('sounds/recover.wav')" : "audio.newSource('sounds/recover.wav', 'static')", #Breakout
	"audio.newSource('sounds/high_score.wav')" : "audio.newSource('sounds/high_score.wav', 'static')", #Breakout
	"audio.newSource('sounds/pause.wav')" : "audio.newSource('sounds/pause.wav', 'static')", #Breakout
	"audio.newSource('sounds/music.wav')" : "audio.newSource('sounds/music.wav', 'static')", #Breakout
	"graphics.setColor(103, 255, 255, 255)":"graphics.setColor(103/255, 255/255, 255/255, 255/255)", #Breakout
	"self.psystem:setAreaSpread('normal', 10, 10)" : "self.psystem:setEmissionArea('normal', 10, 10)", #Breakout
	"['r'] = 99,":"['r'] = 99/255,", #Breakout
	"['g'] = 155,":"['g'] = 155/255,", #Breakout
	"['b'] = 255\n":"['b'] = 255/255\n,", #Breakout
	"['r'] = 106,":"['r'] = 106/255,", #Breakout
	"['g'] = 190,":"['g'] = 190/255,", #Breakout
	"['b'] = 47\n":"['b'] = 47/255\n", #Breakout
	"['r'] = 217,":"['r'] = 217/255,", #Breakout
	"['g'] = 87,":"['g'] = 87/255,", #Breakout
	"['b'] = 99\n":"['b'] = 99/255\n", #Breakout
	"['r'] = 215,":"['r'] = 215/255,", #Breakout
	"['g'] = 123,":"['g'] = 123/255,", #Breakout
	"['b'] = 186\n":"['b'] = 186/255\n", #Breakout
	"['r'] = 251,":"['r'] = 251/255,", #Breakout
	"['g'] = 242,":"['g'] = 242/255,", #Breakout
	"['b'] = 54\n":"['b'] = 54/255\n", #Breakout
	#find a solution for Breakout 10: main.lua:216: Using deprecated function: love.filesystem.exists (replaced by love.filesystem.getInfo),
	#find a solution for Breakout 10: src/states/StartState.lua:24: attempt to index local 'params' (a nil value)
	"opacity = 0\n" : "opacity = 0/255\n", #match3
	"graphics.setColor(255, 255, 255, bird.opacity)" : "graphics.setColor(255/255, 255/255, 255/255, bird.opacity)", #match3
	"graphics.setColor(255, 255, 255, 128)" : "graphics.setColor(255/255, 255/255, 255/255, 128/255)", #match3
	"graphics.setColor(255, 0, 0, 234)" : "graphics.setColor(255/255, 0, 0, 234/255)", #match3
	"audio.newSource('sounds/music3.mp3')" : "audio.newSource('sounds/music3.mp3', 'static')", #match3
	"audio.newSource('sounds/error.wav')" : "audio.newSource('sounds/error.wav', 'static')", #match3
	"audio.newSource('sounds/match.wav')" : "audio.newSource('sounds/match.wav', 'static')", #match3
	"audio.newSource('sounds/clock.wav')" : "audio.newSource('sounds/clock.wav', 'static')", #match3
	"audio.newSource('sounds/game-over.wav')" : "audio.newSource('sounds/game-over.wav', 'static')", #match3
	"audio.newSource('sounds/next-level.wav')" : "audio.newSource('sounds/next-level.wav', 'static')", #match3
	"[1] = {217, 87, 99, 255}" : "[1] = {217/255, 87/255, 99/255, 255/255}", #match3
	"[2] = {95, 205, 228, 255}" : "[2] = {95/255, 205/255, 228/255, 255/255}", #match3
	"[3] = {251, 242, 54, 255}" : "[3] = {251/255, 242/255, 54/255, 255/255}", #match3
	"[4] = {118, 66, 138, 255}" : "[4] = {118/255, 66/255, 138/255, 255/255}", #match3
	"[5] = {153, 229, 80, 255}" : "[5] = {153/255, 229/255, 80/255, 255/255}", #match3
	"[6] = {223, 113, 38, 255}" : "[6] = {223/255, 113/255, 38/255, 255/255}", #match3
	"graphics.setColor(0, 0, 0, 128)" : "graphics.setColor(0, 0, 0, 128/255)", #match3
	"graphics.setColor(99, 155, 255, 255)" : "graphics.setColor(99/255, 155/255, 255/255, 255/255)", #match3
	"graphics.setColor(48, 96, 130, 255)" : "graphics.setColor(48/255, 96/255, 130/255, 255/255)", #match3
	"graphics.setColor(34, 32, 52, 255)" : "graphics.setColor(34/255, 32/255, 52/255, 255/255)", #match3
	"graphics.setColor(95, 205, 228, 200)" : "graphics.setColor(95/255, 205/255, 228/255, 200/255)", #match3
	"graphics.setColor(255, 255, 255, self.transitionAlpha)" : "graphics.setColor(255/255, 255/255, 255/255, self.transitionAlpha/255)", #match3
	"graphics.setColor(255, 255, 255, 96)" : "graphics.setColor(255/255, 255/255, 255/255, 96/255)", #match3
	"graphics.setColor(217, 87, 99, 255)" : "graphics.setColor(217/255, 87/255, 99/255, 255/255)", #match3
	"graphics.setColor(172, 50, 50, 255)" : "graphics.setColor(172/255, 50/255, 50/255, 255/255)", #match3
	"graphics.setColor(56, 56, 56, 234)" : "graphics.setColor(56/255, 56/255, 56/255, 234/255)", #match3
	"math.random(255)\n":"math.random(255)/255\n", #AlienMario
	"audio.newSource('sounds/jump.wav')":"audio.newSource('sounds/jump.wav', 'static')", #AlienMario
	"audio.newSource('sounds/death.wav')":"audio.newSource('sounds/death.wav', 'static')", #AlienMario
	"audio.newSource('sounds/powerup-reveal.wav')":"audio.newSource('sounds/powerup-reveal.wav', 'static')", #AlienMario
	"audio.newSource('sounds/pickup.wav')":"audio.newSource('sounds/pickup.wav', 'static')", #AlienMario
	"audio.newSource('sounds/empty-block.wav')":"audio.newSource('sounds/empty-block.wav', 'static')", #AlienMario
	"audio.newSource('sounds/kill.wav')":"audio.newSource('sounds/kill.wav', 'static')", #AlienMario
	"audio.newSource('sounds/kill2.wav')":"audio.newSource('sounds/kill2.wav', 'static')", #AlienMario
	"audio.newSource('sounds/music.mp3')":"audio.newSource('sounds/music.mp3', 'static')", #The Legend of Zelda
	"audio.newSource('sounds/sword.wav')":"audio.newSource('sounds/sword.wav', 'static')", #The Legend of Zelda
	"audio.newSource('sounds/hit_enemy.wav')":"audio.newSource('sounds/hit_enemy.wav', 'static')", #The Legend of Zelda
	"audio.newSource('sounds/hit_player.wav')":"audio.newSource('sounds/hit_player.wav', 'static')", #The Legend of Zelda
	"audio.newSource('sounds/door.wav')":"audio.newSource('sounds/door.wav', 'static')", #The Legend of Zelda
	"setColor(34, 34, 34, 255)":"setColor(34/255, 34/255, 34/255, 255/255)", #The Legend of Zelda
	"setColor(175, 53, 42, 255)":"setColor(175/255, 53/255, 42/255, 255/255)", #The Legend of Zelda
	"setColor(255, 255, 255, 255)":"setColor(255/255, 255/255, 255/255, 255/255)", #The Legend of Zelda
	#"through\n\tlove.graphics.stencil":"through\n\tlove.graphics.setCanvas({canvas, stencil=true})\n\tlove.graphics.stencil", #The Legend of Zelda <--- not working
	# even if the line above was working, it creates a new bug: the player won't be drawn
	# find a solution for: src/states/entity/player/PlayerSwingSwordState.lua:95: attempt to index field 'swordHurtbox' (a nil value)
	"setColor(0, 255, 0, 255)":"setColor(0/255, 255/255, 0/255, 255/255)", # Angry Birds
	"setColor(255, 0, 0, 255)":"setColor(255/255, 0/255, 0/255, 255/255)", # Angry Birds
	"math.random(255),":"math.random(255)/255,", # Angry Birds
	"audio.newSource('sounds/break1.wav'),":"audio.newSource('sounds/break1.wav', 'static'),", # Angry Birds
	"audio.newSource('sounds/break2.wav'),":"audio.newSource('sounds/break2.wav', 'static'),", # Angry Birds
	"audio.newSource('sounds/break3.mp3'),":"audio.newSource('sounds/break3.mp3', 'static'),", # Angry Birds
	"audio.newSource('sounds/break4.wav'),":"audio.newSource('sounds/break4.wav', 'static'),", # Angry Birds
	"audio.newSource('sounds/break5.wav'),":"audio.newSource('sounds/break5.wav', 'static'),", # Angry Birds
	"audio.newSource('sounds/bounce.wav'),":"audio.newSource('sounds/bounce.wav', 'static'),", # Angry Birds
	"graphics.setColor(64, 64, 64, 200)":"graphics.setColor(64/255, 64/255, 64/255, 200/255)", # Angry Birds
	"graphics.setColor(200, 200, 200, 255)":"graphics.setColor(200/255, 200/255, 200/255, 255/255)", # Angry Birds
	"graphics.setColor(255, 80, 255, (255 / 12) * i)":"graphics.setColor(255/255, 80/255, 255/255, ((255 / 12) * i)/255)", # Angry Birds
	"audio.newSource('sounds/field_music.wav'),":"audio.newSource('sounds/field_music.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/battle_music.mp3'),":"audio.newSource('sounds/battle_music.mp3', 'static'),", #Pokemon
	"audio.newSource('sounds/blip.wav'),":"audio.newSource('sounds/blip.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/powerup.wav'),":"audio.newSource('sounds/powerup.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/hit.wav'),":"audio.newSource('sounds/hit.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/run.wav'),":"audio.newSource('sounds/run.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/heal.wav'),":"audio.newSource('sounds/heal.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/exp.wav'),":"audio.newSource('sounds/exp.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/levelup.wav'),":"audio.newSource('sounds/levelup.wav', 'static'),", #Pokemon
	"audio.newSource('sounds/intro.mp3')":"audio.newSource('sounds/intro.mp3', 'static')", #Pokemon
	"graphics.setColor(24, 24, 24, 255)":"graphics.setColor(24/255, 24/255, 24/255, 255/255)", #Pokemon
	"graphics.setColor(45, 184, 45, 124)":"graphics.setColor(45/255, 184/255, 45/255, 124/255)", #Pokemon
	"graphics.clear(188, 188, 188, 255)":"graphics.clear(188/255, 188/255, 188/255, 255/255)", #Pokemon
	"graphics.clear(214, 214, 214, 255)":"graphics.clear(214/255, 214/255, 214/255, 255/255)", #Pokemon
	"{r = 189, g = 32, b = 32}":"{r = 189/255, g = 32/255, b = 32/255}", #Pokemon
	"{r = 32, g = 32, b = 189}":"{r = 32/255, g = 32/255, b = 189/255}", #Pokemon
	"love.graphics.setColor(56, 56, 56, 255)":"love.graphics.setColor(56/255, 56/255, 56/255, 255/255)", #Pokemon
	"{opacity = 0}":"{opacity = 0/255}", #Pokemon
	"r = 255, g = 255, b = 255":"r = 255/255, g = 255/255, b = 255/255", #Pokemon
	#"":"",
}

#=============================
# function correct
#=============================
errors = 0 #count the number of errors to warn the user at the end of the script
total_corrections = 0

def file_correction(file_path):
	global total_corrections

	try:
		data = open(file_path, "r") 	#read the file in a non destructive test.

		text_lines = list() 	#create a list to save all lines inside of it
		term_found = False
		corrections = 0

		for line in  data:
			for term in terms:		#check if one of the terms from the dictionary can be found in the line we're testing
				if term in line:
					term_found = True
					total_corrections += 1
					corrections += 1
					line = line.replace(term, terms[term])		#replace the term found for the term in it's meaning

			text_lines.append(line)		#write the line (replaced or not) to the list

		data.close()

	except:
		# files like png, wav and etc. are not readable.
		# It is still useful to handle the files read by the "correct the files in the main folder"
		# DO NOT DELETE THIS!
		print("\033[31mNot a readable file.\033[m")
		return


	try:
		if term_found == True:
			data = open(file_path, "w") 	#read the file ready to rewrite the file. this might be destructive.
			for line in text_lines:
				data.write(line)

			data.close()
			print(f"\033[33m{corrections} Line/s corrected successfully.\033[m")

		else:
			print("\033[32mNo corrections needed.\033[m")

	except:
		global errors
		errors =+1
		print("\033[41m COULD NOT CORRECT THIS FILE \033[m")


#########################################################
# Folder, subfolders and files Info
#########################################################

try:
	path = " ".join(sys.argv[1:]) #path used in case it is passed as argument when running this script
	
	try:
		itens = os.listdir(path)
	except FileNotFoundError:
		#print(path)
		print("\033[41m couldn't find this directory \033[m")
		print("Please verify the specified path")
		print("in case you tried to specify a file, this is not fully supported yet, although it may occasionally work")
		quit()
	except NotADirectoryError: # < might not work
		if os.path.isfile(path):
			print(path, end=" -> ")
			file_correction(path)
			quit()
		else:
			print("\033[41m couldn't find this directory \033[m")
			print("Please verify the specified path")			
			quit()
		
except IndexError: # path in case there's no argument.
	print(f"Using the current location of {__file__}:")
	path = os.getcwd()  #the path will be the path where this script is located
	print(path)
	itens = os.listdir(path)

if "\\" in path:		#it will work differently in Windows or Unix-like operating systems
	back_slash = "\\"
else:
	back_slash = "/"


files = list()		# all files in main folder
folders = list()	# .lua files in subfolders


for item in itens:		# It will be used to create the titles on output
	pre_path = path
	if pre_path[-1] != back_slash:
		pre_path = pre_path + back_slash
	
	item = pre_path + item
	
	if os.path.isdir(item):
		folders.append(item)

	elif os.path.isfile(item): 	#It will be used to run the script in the main folder
		files.append(item)


#=============================
# correct the files in the main folder
#=============================
title(path)
for file_ in files:
	if file_ != path + back_slash + __file__:		#prevents the script of rewriting itself.
		print(f"{file_}", end=" -> ")
		file_correction(file_)		#call the function to correct the file


#=============================
# correct the files in the subfolders
#=============================
# **/       every file and dir under "path"
# *.lua     every file that ends with '.lua'
files_subfolder = glob.glob(path + '/**/*.lua', recursive=True) #search for all .lua files in the subfolders

for folder in folders:
	#create a formated title in output with the title of the folder, but not the whole path.
	title(folder.replace(path, ""))
	
	for file_ in files_subfolder:
		#print(folder.replace(path,"")[1:], " ", file_.replace(path,"").split(back_slash)[1])
		if folder.replace(path,"")[1:] == file_.replace(path,"").split(back_slash)[1]: #compare the name of the folder and the path to the file, to group them on output
			print(file_.replace(path,""), end=" -> ")
			file_correction(file_)	#call the function to correct the file


##############################
# The end:
##############################
if errors == 0:
	print(f"\n\n\033[32mI'm done :) \n{total_corrections} lines corrected \033[m")

else:
	print(f"""\n\n\033[33mI'm done, but #{errors} error/s were found. 
	\nMaybe those files were set to \"read-only\" mode or this scritp has no permission to write in here.
	\nThe files should be corrected manually, or they might not work correctly.
	\nBut {total_corrections} lines were corrected \033[m""")
