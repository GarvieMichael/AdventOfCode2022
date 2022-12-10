# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
text_file = open('Day3/Day3.txt', 'r')
items = text_file.readlines()
shared_letters = []
first_half= []
second_half = []
items_length = len(items)
last_i = 0

for i in range(0, items_length, 1):
    items[i] = items[i].strip()

for i in range(0, items_length, 1):
    item = items[i]
    item_length = len(item)
    half_length = int(item_length/2)
    first_half = item[0:half_length]
    first_length = len(first_half)
    second_half = item[half_length:item_length]
    second_length = len(second_half)
    # if item_length % 2:
    #     first_half = item[0:len(item)/2]
    #     second_half = item[len(item)/2:len(item)]
    # else:
    #     first_half = item[0:len(item)/2]
    #     second_half = item[len(item)/2:len(item)]
    for k in range(0, half_length, 1):
        if first_half[k] in second_half:
            # shared_letters.append(first_half[k])
            if (not shared_letters) and (first_half[k] not in shared_letters):
                shared_letters.append(first_half[k])
                last_i = i
                break
            elif ((last_i != i)) or (first_half[k] not in shared_letters[-1]):
                shared_letters.append(first_half[k])
                last_i = i
                break
    if (len(shared_letters) != (i+1)):
        print("shared letters = " + str(len(shared_letters)) + "and I equals " + str(i+1))

# print(items)
# print(shared_letters)

letter_priorities = []

def calculate_priority(shared_letters, letter_priorities):
    for each in shared_letters:
        if each.islower():
            letter_priorities.append(int(str(ord(each)&31)))
        else:
            letter_priorities.append(int(str(ord(each)&31)) + 26)

calculate_priority(shared_letters, letter_priorities)

# print(letter_priorities)
final_priority = sum(letter_priorities)
print(final_priority)