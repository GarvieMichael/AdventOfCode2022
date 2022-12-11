# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
text_file = open('Day4/Day4.txt', 'r')
assignments = text_file.readlines()
assignments_length = len(assignments)
overlaps = 0

for i in range(0, assignments_length, 1):
    assignments[i] = assignments[i].strip()

for each in assignments:
    first_assignment = each.split(",")[0]
    second_assignment = each.split(",")[1]

    start_first_range = int(first_assignment.split("-")[0])
    end_first_range = int(first_assignment.split("-")[1])

    start_second_range = int(second_assignment.split("-")[0])
    end_second_range = int(second_assignment.split("-")[1])
    
    if ((start_first_range <= start_second_range) and (end_first_range >= end_second_range)) or ((start_second_range <= start_first_range) and (end_second_range >= end_first_range)):
        overlaps += 1

    # print(start_first_range)
    # print(end_first_range)
    # print(start_second_range)
    # print(end_second_range)
    # print("\n")

print(overlaps)