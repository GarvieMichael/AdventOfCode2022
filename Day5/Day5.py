import pprint as pp
# import numpy as np
text_file = open("Day5/Day5_diagram.txt")
crates = text_file.readlines()

rules_file = open("Day5/Day5.txt")
rules = rules_file.readlines()

import re
## re.match or re.findall <--- looks for multiple matches for the pattern across the same line
stack = [re.findall('([A-Z]|\s{3})\s?', x.strip('[]')) for x in crates]
transposed = [[row[i] if len(row[i]) == 1 else '' for row in stack] for i in range(len(stack[0]))]
transposed = [list(reversed(row)) for row in transposed]
transposed = [[x for x in row if len(x) > 0] for row in transposed]

print("\n")
pp.pprint(transposed)

destination = []
pr = []
for each in rules:
    parsed_rules = re.match("move (\d+) from (\d+) to (\d+)", each)

    # print(parsed_rules[1])
    # print(parsed_rules[2])
    # print(parsed_rules[3])

    pr.append(list(map(int, re.findall('(\d+)', each))))
    # print(pr)

for rule in pr:
    for i in range(0, rule[0]):
        temp_stack = transposed[rule[1]-1].pop()
        transposed[rule[2]-1].append(temp_stack)


        print(transposed)
    print(each)

    # crate = transposed.pop()
    # destination.append(crate)
    # count = 5
    # index = len(transposed[1]) - count
    # crate = transposed.pop(index) #<--- here it will pop not from the end, but from a fixed index from the bottom.

final_answer = ''
for each in transposed:
    final_answer = final_answer + each[-1]

print(final_answer)





# a = [1, 2, 3, 4, 5, 6, 7]
# b = a.pop()
# assert b == 7
# c = a.pop(0)
# assert c == 1
# d = a.pop(-1)
# assert d == 6
# e = a.pop(2)
# assert e == 4

# pp.pprint(transposed)