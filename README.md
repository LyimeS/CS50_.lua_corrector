# CS50 .lua corrector
A python script to update the .lua files shared by CS50 to be read by Löve2D 11.3

# What you should know before using it:
* This script runs using Python 3. 
* I intend to port this script to Windows, but, right now, it is only working in Linux (and maybe in MacOS, but I didn't test it).
* It is a good idea to have a backup of the files before running this script. It should be safe to run it, but... you know... just in case. Or you can download the files again from GitHub. That's up to you. 

# How to use it:
1. Paste the script *correct.py* in the main directory of a project shared by CS50 <sup>(see notes bellow)</sup>
2. Run the script. Open the main directory in terminal and type `python3 "correct.py"` 

## The meaning of "main directory" in here:
Let's suppose you want to correct the files from the [mario-demo](https://github.com/cs50/mario-demo) game. You'll download the folder *mario-demo* containing 25 folders + 2 files. The *correct.py* should be pasted in *mario-demo*.
### Why?
This script will open all files in *mario-demo*, and all files in the subfolders "lovedemo", "mario-0", "mario-0-exercise", "mario-1", and so on. **Please note:** It won't search for the files in the subfolders of those subfolders. e.g.:  
`mario-demo / lovedemo / graphics`  
this script will read the files in *"mario-demo"* and *"lovedemo"*, but it will **not** look inside the *"graphics"* folder, until I found some reason to do so. 

## What was I supposed to see in its output?
Blocks containing the files the script was able to read, and what happened to them. 

# Things you may be wondering:
## What projects from CS50 does this script corrects?
* pong
* fifty-bird
* mario-demo

## I have found a bug.
Well, I'm sorry to hear that. Feel free to report it in "Issues" section, but I just need you to keep mind that my programming skills are just like my art skills: almost nonexistent. So it might take a while before I can solve it (if I'm able to do so. Please root for me).

## Why, in Merlin's name, did you do this extension?

## Do you call that garbage as "code"?
"I'm not a real programmer, I just glue stuff together"
