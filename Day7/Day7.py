import pprint as pp
import numpy as np
from treelib import Node, Tree
import re
text_file = open("Day7/Day7.txt")
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
            tree.create_node(re.match("\$ cd (\/)", each)[1], re.match("\$ cd (\/)", each)[1]) # root
            last_dir.append(re.match("\$ cd (\/)", each)[1])
        elif each == '$ ls':
            listing = True
        elif (listing == True) and (each[0] != '$'):
            if each.startswith("dir"):
                if len(last_dir) > 1:
                    tree.create_node(re.match("dir ([a-zA-Z]*)", each)[1], re.match("dir ([a-zA-Z]*)", each)[1] + "_" + last_dir[-1], parent = last_dir[-1] + "_" + last_dir[-2])
                else:
                  tree.create_node(re.match("dir ([a-zA-Z]*)", each)[1], re.match("dir ([a-zA-Z]*)", each)[1] + "_" + last_dir[-1], parent = last_dir[-1])  
            else:
                temp_file = re.split("\s",each)
                if len(last_dir) > 1:
                    tree.create_node(temp_file[1], temp_file[1] + "_" + last_dir[-1], parent = last_dir[-1] + "_" + last_dir[-2], data = temp_file[0])
                else:
                    tree.create_node(temp_file[1], temp_file[1] + "_" + last_dir[-1], parent = last_dir[-1], data = temp_file[0])
            
                
        elif (listing == True) and (each[0] == '$'):
            if each == '$ cd ..':
                last_dir.pop()
            elif each[2:4] == 'cd':
                listing = False
                last_dir.append(re.match("\$ cd ([a-zA-Z]*)", each)[1])

strip_the_commands(directories)
read_the_commands(directories, files, dirs, last_dir)
dirs.show()
max_successors = 0
for each in Tree.all_nodes_itr(dirs):
    if len(each.successors(dirs.identifier)) > max_successors:
        max_successors = len(each.successors(dirs.identifier))

for i in range(1, max_successors+1, 1):
    for each in Tree.all_nodes_itr(dirs):
        if (len(each.successors(dirs.identifier)) == i) and (each.tag != '/'):
            for every in each.successors(dirs.identifier):
                if dirs.get_node(each.identifier).data == None:
                    dirs.get_node(each.identifier).data = int(dirs.get_node(every).data)
                else:
                    dirs.get_node(each.identifier).data += int(dirs.get_node(every).data)

for i in range(1, max_successors+1, 1):
    for each in Tree.all_nodes_itr(dirs):
        if (len(each.successors(dirs.identifier)) == i) and (each.tag == '/'):
            for every in each.successors(dirs.identifier):
                if dirs.get_node(each.identifier).data == None:
                    dirs.get_node(each.identifier).data = int(dirs.get_node(every).data)
                else:
                    dirs.get_node(each.identifier).data += int(dirs.get_node(every).data)                   
    
total_size = 0
for each in Tree.all_nodes_itr(dirs):
    pp.pprint(each)
    if (len(each.successors(dirs.identifier)) > 0) and (each.tag != '/'):
        if each.data <= 100000:
            total_size += each.data
    

print(total_size)