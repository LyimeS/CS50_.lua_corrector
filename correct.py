#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import os
import glob

#########################################################
# FORMAT Title
#########################################################
def title (txt):
	print("-" * len(txt), end="--\n")
	print("\033[44m", end="")
	print(" " + txt + " ", end="")
	print("\033[m")
	print("-" * len(txt), end="--\n")

#########################################################
# File correction
#########################################################
#=============================
# dictionary of terms to be corrected
#=============================
terms = {
	"getPixelScale": "getDPIScale", 
	"love.graphics.clear(40, 45, 52, 255)": "love.graphics.clear(40/255, 45/255, 52/255, 1)",  # pong
	"love.graphics.clear(108, 140, 255, 255)": "love.graphics.clear(108/255, 140/255, 255/255, 255/255)", # mario
	"music = love.audio.newSource('music/overworld.mp3')": "music = love.audio.newSource('music/overworld.mp3', 'static')", # mario
	"love.audio.newSource('sounds/paddle_hit.wav')" : "love.audio.newSource('sounds/paddle_hit.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/score.wav')" : "love.audio.newSource('sounds/score.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/wall_hit.wav')" : "love.audio.newSource('sounds/wall_hit.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/confirm.wav')" : "love.audio.newSource('sounds/confirm.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/select.wav')" : "love.audio.newSource('sounds/select.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/no-select.wav')" : "love.audio.newSource('sounds/no-select.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/brick-hit-1.wav')" : "love.audio.newSource('sounds/brick-hit-1.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/brick-hit-2.wav')" : "love.audio.newSource('sounds/brick-hit-2.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/hurt.wav')" : "love.audio.newSource('sounds/hurt.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/victory.wav')" : "love.audio.newSource('sounds/victory.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/recover.wav')" : "love.audio.newSource('sounds/recover.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/high_score.wav')" : "love.audio.newSource('sounds/high_score.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/pause.wav')" : "love.audio.newSource('sounds/pause.wav', 'static')", #Breakout
    "love.audio.newSource('sounds/music.wav')" : "love.audio.newSource('sounds/music.wav', 'static')", #Breakout
    "love.graphics.setColor(103, 255, 255, 255)":"love.graphics.setColor(103/255, 255/255, 255/255, 255/255)", #Breakout
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

}

#=============================
# function correct
#=============================
errors = 0 #count the number of errors to warn the user at the end of the script

def file_correction(file_path):
	
	try:
		data = open(file_path, "r") 	#read the file in a non destructive test.
	
		text_lines = list() 	#create a list to save all lines inside of it
		term_found = False
		
		for line in  data:
			for term in terms:		#check if one of the terms from the dictionary can be found in the line we're testing 
				if term in line:
					term_found = True
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
			print("\033[33mLine/s corrected successfully.\033[m")
		
		else:
			print("\033[32mNo corrections needed.\033[m")
	
	except:
		global errors
		errors =+1
		print("\033[41mCOULDN'T CORRECT THIS FILE!\033[m")



#########################################################
# Folder, subfolders and files Info
#########################################################
path = os.getcwd()
itens = os.listdir(path)


if "\\" in path:		#it will work differently in Windows or Unix-like operating systems
	back_slash = "\\"
else:
	back_slash = "/"


files = list()
folders = list()


for item in itens:		# It will be used to create the titles on output
	if os.path.isdir(item):
		folders.append(item)
	
	elif os.path.isfile(item): 	#It will be used to run the script in the main folder
		files.append(item)
	

#=============================
# correct the files in the main folder
#=============================
title(path)
for file_ in files:
	if file_ != __file__:		#prevents the script of rewriting itself.
		print(f"{file_}", end=" -> ")
		file_correction(path + back_slash + file_)		#call the function to correct the file



#=============================
# correct the files in the subfolders
#=============================	
# **/       every file and dir under "path"
# *.txt     every file that ends with '.lua'
files_subfolder = glob.glob(path + '/**/*.lua', recursive=True) #search for all .lua files in the subfolders

for folder in folders:
	title(folder)		#create a title in output with the 
	for file_ in files_subfolder:
		if file_.replace(path, "")[0:len(folder) + 1] == back_slash + folder: 		#compare the name of the folder and the path to the file.
			print(file_.replace(path, ""), end=" -> ")
			file_correction(file_)		#call the function to correct the file


##############################
# The end:
##############################
if errors == 0:
	print("\n\n\033[32mI'm done :)\033[m")
	
else:
	print(f"\n\n\033[33mI'm done, but #{errors} error/s were found. \nThis may be caused because the files were set to \"read only\" mode.\nThey should be corrected manually\033[m")


