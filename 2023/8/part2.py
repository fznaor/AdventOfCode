import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

directions = [x for x in lines[0].strip()]
nodes = {}

for line in [line.strip() for line in lines[2:]]:
    key = line.split()[0]
    left = line.split('(')[1].split(', ')[0]
    right = line.split('(')[1].split(', ')[1][:-1]
    nodes[key] = [left, right]

currSteps = []
for key in nodes:
    if key.endswith('A'):
        currSteps.append(key)

stepsArr= []
for currStep in currSteps:
    steps = 0
    i = 0
    while True:
        if directions[i] == 'L':
            currStep = nodes[currStep][0]
        else:
            currStep = nodes[currStep][1]
        steps += 1
        if currStep.endswith('Z'):
            stepsArr.append(steps)
            break
        i += 1
        if i >= len(directions):
            i = 0
print(math.lcm(*stepsArr))