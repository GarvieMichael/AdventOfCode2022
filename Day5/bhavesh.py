from pprint import pprint
s1 = ['H','B','V','W','N','M','L','P']
s2 = ['M','Q','H']
s3 = ['N','D','B','G','F','Q','M','L']
s4 = ['Z','T','F','Q','M','W','G']
s5 = ['M','T','H','P']
s6 = ['C','B','M','J','D','H','G','T']
s7 = ['M','N','B','F','V','R']
s8 = ['P','L','H','M','R','G','S']
s9 = ['P','D','B','C','N']
stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
# test data
# s1 = [ 'Z', 'N' ]
# s2 = [ 'M', 'C', 'D' ]
# s3 = [ 'P' ]
# stacks = [ s1, s2, s3 ]
def process(quantity, fromStack, toStack):
  # pprint(stacks)
  # print("")
  for i in range(quantity):
    if len(stacks[fromStack]) > 0:
      stacks[toStack].append(stacks[fromStack].pop())
  # pprint(stacks)
rules = []
with open('./Day5/Day5.txt') as f:
  for line in f.readlines():
    rule = []
    for value in line.split(','):
      rule.append(int(value.strip()))
    rules.append(rule)
for (q, fromStack, toStack) in rules:
  process(q, fromStack - 1 , toStack - 1)
output = ''
for stack in stacks:
  output += stack[-1]
pprint(output)