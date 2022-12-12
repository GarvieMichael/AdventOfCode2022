# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
import pprint as pp
import numpy as np
text_file = open("Day5/Day5_diagram.txt")
crates = text_file.readlines()

crates.pop()
crates_length = len(crates)
box_stacks = 0
box_max_length = 0
# stacks = 3
stacks = 9
box_max_length = (stacks * 4) - 1


for i in range(0, crates_length, 1):
    crates[i] = crates[i].strip("\n")

actual_total_boxes = box_max_length//4

stacked_boxes = np.empty((stacks,actual_total_boxes), dtype=object)
clean_stacks = np.empty((stacks,actual_total_boxes), dtype=str)
letter_count = 0
number_count = 0
array_count = 0
for each in reversed(crates):
    while letter_count < box_max_length:
        if each[1+letter_count] != " ":
            stacked_boxes[array_count][number_count] = each[1+letter_count]
        # if each[5] != " ":
        #     stacked_boxes[1][letter_count] = each[5]
        # if each[9] != " ":
        #     stacked_boxes[2][letter_count] = each[9]
        letter_count += 4
        array_count +=1
        # number_count += 1
    array_count = 0
    number_count += 1
    letter_count = 0

# pp.pprint(stacked_boxes)


for i in range(0, len(stacked_boxes), 1):
    for k in range(0, len(stacked_boxes[i]), 1):
        if stacked_boxes[i][k] != None:
            clean_stacks[i][k] = stacked_boxes[i][k]

# for i in range(0, len(clean_stacks), 1):
#     for k in range(0, len(clean_stacks[i]), 1):
#         if stacked_boxes[i][k] == '':
#             np.delete(clean_stacks[i][k])
    
# clean_stacks = np.deslete(stacked_boxes, np.where(stacked_boxes == None))

# pp.pprint(stacked_boxes)
pp.pprint(clean_stacks)

# print(crates)
# print(box_stacks)
# print(box_max_length)