# /usr/bin/env /bin/python3 /home/michaelgarvie/.vscode/extensions/ms-python.python-2022.8.1/pythonFiles/lib/python/debugpy/launcher 42419 -- /home/michaelgarvie/Documents/Work_Documentation/AdventOfCode2022/Day1/Day1.py
text_file = open('Day2/Day2.txt', 'r')
RPS = text_file.readlines()
their_scores = []
my_scores = []
versus_scores = []
my_final_scores = []
my_score = 0
their_score = 0
their_final_scores =[]

def calculate_score_for_moves(moves, output):
    for x in moves:
        if x == 'A' or x == 'X':
            output.append(1)
        elif x == 'B' or x == 'Y':
            output.append(2)
        elif x == 'C' or x == 'Z':
            output.append(3)
        else:
            output.append(0)

their_moves = []
my_moves = []

for x in RPS:
    their_moves.append(x[0])
    my_moves.append(x[2])
    
moves = len(my_moves)

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

#Part 2
# For me:
# X = lose
# Y means draw
# Z means win

my_new_moves = []

def calculate_part_two_moves(mine, theirs, my_new_moves):
    for i in range(0, moves, 1):
        if (mine[i] == 'Y' and theirs[i] == 'A'):
            my_new_moves.append('X') #if I must draw
        elif (mine[i] == 'Y' and theirs[i] == 'B'):
            my_new_moves.append('Y') #if I must draw
        elif (mine[i] == 'Y' and theirs[i] == 'C'):
            my_new_moves.append('Z') #if I must draw

        elif (mine[i] == 'Z' and theirs[i] == 'A'):
            my_new_moves.append('Y') #if I must win
        elif (mine[i] == 'Z' and theirs[i] == 'B'):
            my_new_moves.append('Z') #if I must win
        elif (mine[i] == 'Z' and theirs[i] == 'C'):
            my_new_moves.append('X') #if I must win
        
        elif (mine[i] == 'X' and theirs[i] == 'A'):
            my_new_moves.append('Z') #if I must lose
        elif (mine[i] == 'X' and theirs[i] == 'B'):
            my_new_moves.append('X') #if I must lose
        elif (mine[i] == 'X' and theirs[i] == 'C'):
            my_new_moves.append('Y') #if I must lose
    return my_new_moves

my_new_moves = calculate_part_two_moves(my_moves, their_moves, my_new_moves)

# For part one, use part one's mine
def calculate_score_for_versus(mine, theirs):
    for i in range(0, moves, 1):
        if (mine[i] == 'X' and theirs[i] == 'A') or (mine[i] == 'Y' and theirs[i] == 'B') or (mine[i] == 'Z' and theirs[i] == 'C'): #Draws
            versus_scores.append(3)
        elif (mine[i] == 'X' and theirs[i] == 'B') or (mine[i] == 'Y' and theirs[i] == 'C') or (mine[i] == 'Z' and theirs[i] == 'A'): #Losses
            versus_scores.append(0)
        elif (mine[i] == 'X' and theirs[i] == 'C') or (mine[i] == 'Y' and theirs[i] == 'A') or (mine[i] == 'Z' and theirs[i] == 'B'): #Wins
            versus_scores.append(6)
        else:
            versus_scores.append(0)

calculate_score_for_moves(their_moves, their_scores)
calculate_score_for_moves(my_new_moves, my_scores)
calculate_score_for_versus(my_new_moves, their_moves)

def calculate_score(mine, theirs, versus, my_score, their_score):
    for i in range(0, moves, 1):
        my_final_scores.append(mine[i] + versus[i])
        their_final_scores.append(theirs[i] + versus[i])
    my_score = sum(my_final_scores)
    their_score = sum(their_final_scores)
    return my_score, their_score
    
        
my_score, their_score = calculate_score(my_scores, their_scores, versus_scores, my_score, their_score)










print(my_scores)

print(their_scores)

print(versus_scores)

print(my_final_scores)

print(their_final_scores)

print(my_score)

print(their_score)




