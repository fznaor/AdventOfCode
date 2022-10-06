file1 = open('input.txt', 'r')
lines = file1.readlines()

orders = []
directions = ['N', 'E', 'S', 'W']
currDir = 1

eastMove = 0
northMove = 0

for line in lines:
    line = line.rstrip()
    direction = line[0]
    value = int(line[1:])
    
    if direction == 'F':
        direction = directions[currDir]
    elif direction == 'L':
        currDir -= value // 90
        currDir %= 4
    elif direction == 'R':
        currDir += value // 90
        currDir %= 4
    
    if direction == 'N':
        northMove += value
    elif direction == 'S':
        northMove -= value
    elif direction == 'W':
        eastMove -= value
    elif direction == 'E':
        eastMove += value
    
print(abs(eastMove) + abs(northMove))