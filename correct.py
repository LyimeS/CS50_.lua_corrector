# -*- coding: utf-8 -*- 

import os

#########################################################
# FORMAT Title
#########################################################
def title (txt):
	print("-" * len(txt))
	print("\033[45m", end="")
	print(txt, end="")
	print("\033[m")
	print("-" * len(txt))

#########################################################
# File correction
#########################################################
#=============================
# dictionary of terms to be corrected
#=============================
terms = {
	"getPixelScale": "getDPIScale",
	"love.graphics.clear(40, 45, 52, 255)": "love.graphics.clear(40/255, 45/255, 52/255, 1)"
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
		print("\033[31mNot a readable file.\033[m")		#files like png, wav and etc. are not readable
		return
	

	try:
		if term_found == True:
			data = open(file_path, "w") 	#read the file ready to rewrite the file. this might be destructive.
			for line in text_lines:
				data.write(line)
			
			data.close()
			print("\033[32mLine corrected successfully.\033[m")
		
		else:
			print("\033[33mNo line to be corrected found.\033[m")
	
	except:
		global errors
		errors =+1
		print("\033[41mCOULDN'T CORRECT THIS FILE!\033[m")



#########################################################
# Folder, subfolders and files Info
#########################################################
path = os.getcwd()
itens = os.listdir(path)

files = list()
folders = list()

for item in itens:
	if os.path.isdir(item):
		#print(f"{item} is a directory")
		folders.append(item)
	
	elif os.path.isfile(item):
		#print(f"{item} is a file")
		files.append(item)
		
	else:
		print(f"Error: I don't know what the hell is {item}.") #I've never seen this error happening. it might be useless.

print(f"found {len(files) -1} files and {len(folders)} subfolders.")



#=============================
# correct the files in the main folder
#=============================
for file_ in files:
	if file_ != __file__:		#prevents the script of rewriting itself.
		print(f"{file_} found in this folder: ", end="")
		file_correction(path + "/" + file_)


#=============================
# correct the files in the subfolders
#=============================
for subfolder in folders:
	files_subfolder = os.listdir(subfolder)
	
	title(subfolder)
	
	for file_ in files_subfolder:
		if os.path.isfile(path + "/" + subfolder + "/" + file_):
			print(f"{file_} found in subfolder: ", end="")
			#print(path + folder + "/" + file_)
			file_correction(path + "/" + subfolder + "/" + file_)
	

##############################
# The end:
##############################
if errors == 0:
	print("\n\n\n\033[32mI'm done :)\033[m")
	
else:
	print(f"\n\n\n\033[33mI'm done, but #{errors} error(s) were found. \nThis may be caused because the files were set to \"read only\" mode.\nThey should be corrected manually\033[m")


