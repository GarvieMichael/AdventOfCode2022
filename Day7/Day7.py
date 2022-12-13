import pprint as pp
import numpy as np
import json as js
text_file = open("Day7/example.txt")
directories = text_file.readlines()
stripped_directories = []
root = '/'
level = 0
files = {}


#Create JSON objects with level, file size, parent and children directories. 

def strip_the_commands(commands):
    for i in range(0, len(commands), 1):
        commands[i] = commands[i].strip()

def read_the_commands(commands, files):
    for each in commands:
        if each == '$ cd /':
            level = 0
        elif each == '$ ls':
            files[level].append(each)


    # pp.pprint(commands)

strip_the_commands(directories)
read_the_commands(directories, files)
pp.pprint(files)
