# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
text_file = open('Day1.txt', 'r')
calorie_array = text_file.readlines()
calorie_array_length = len(calorie_array)

#print(calorie_array)
elf = 0
elves = [ [0]*calorie_array_length for i in range(calorie_array_length)]
elves_totalled = [0 for i in range(calorie_array_length)]
temp_array = []

for x in calorie_array:
    if x == '\n':
        elves.insert(elf, temp_array)
        temp_array=[]
        elf += 1
    elif x == calorie_array[-1]:
        temp_array.append(x)
        elves.insert(elf, temp_array)
    else:
        temp_array.append(x)

temp_array2 = []
elves_final = []
for x in elves:
    # print(x)
    for y in x:
        if isinstance(y, str):
            y = y.strip("\n")
            y = int(y)
            temp_array2.append(y)
        # elves_totalled
    elves_final.append(temp_array2)
    temp_array2 = []
    
# print(elves_final)
elves_final_final = []
for x in elves_final:
    x = sum(x)   
    elves_final_final.append(x)

out = [i for i in elves_final_final if i != 0]

answer = max(out)
max = 0
second = 0
third = 0

for x in out:
    if x > max:
        third = second
        second = max
        max = x
    elif x > second:
        third = second
        second = x
    elif x > third:
        third = x

print(answer

)
index_max = out.index(max)
index_second = out.index(second)
index_third = out.index(third)

second_out = out[index_max] + out[index_second] + out[index_third]

print(second_out)