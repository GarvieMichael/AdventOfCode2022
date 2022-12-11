# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
text_file = open('Day3/Day3.txt', 'r')
items = text_file.readlines()
shared_letters = []
first_half= []
second_half = []
items_length = len(items)
last_i = 0
badges = []

for i in range(0, items_length, 1):
    items[i] = items[i].strip()

for i in range(0, items_length, 3):
    item1 = items[i]
    item2 = items[i+1]
    item3 = items[i+2]

    first_intersection = set(item1).intersection(item2)
    print(first_intersection)
    second_intersection = set(first_intersection).intersection(item3)
    badges.append(list(second_intersection))
print(badges)
print("\n")

badges_output = [item for sublist in badges for item in sublist]

letter_priorities = []

def calculate_priority(badges, letter_priorities):
    for each in badges:
        if each.islower():
            letter_priorities.append(int(str(ord(each)&31)))
        else:
            letter_priorities.append(int(str(ord(each)&31)) + 26)


calculate_priority(badges_output, letter_priorities)

print(letter_priorities)
final_priority = sum(letter_priorities)
print(final_priority)