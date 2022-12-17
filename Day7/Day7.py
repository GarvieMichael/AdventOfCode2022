import pprint as pp
import numpy as np
from treelib import Node, Tree
import re
text_file = open("Day7/example.txt")
directories = text_file.readlines()
stripped_directories = []
root = '/'
level = 0
last_dir = []
files = {}
dirs = Tree()

# Use dictionary with labels 

def strip_the_commands(commands):
    for i in range(0, len(commands), 1):
        commands[i] = commands[i].strip()

def read_the_commands(commands, files, tree, last_dir):
    for each in commands:
        if each == '$ cd /':
            tree.create_node(each[-1], each[-1]) # root
            last_dir.append(each[-1])
        elif each == '$ ls':
            listing = True
        elif (listing == True) and (each[0] != '$'):
            if each.startswith("dir"):
                tree.create_node(each[-1], each[-1], parent = last_dir[-1])
            else:
                temp_file = re.split("\s",each)
                tree.create_node(temp_file[1], temp_file[1], parent = last_dir[-1], data = temp_file[0])
        elif (listing == True) and (each[0] == '$'):
            if each == '$ cd ..':
                last_dir.pop()
            elif each[2:4] == 'cd':
                listing = False
                last_dir.append(each[-1])
            
        # dirs.show()
# pp.pprint(directories)

strip_the_commands(directories)
read_the_commands(directories, files, dirs, last_dir)
print('\n')
dirs.show()
for each in Tree.all_nodes(dirs):
    print(each.tag + " " + str(each.data)) 

