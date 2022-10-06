import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

orders = []
waypoint = np.array([1, 10, 0, 0])

eastMove = 0
northMove = 0

for line in lines:
    line = line.rstrip()
    direction = line[0]
    value = int(line[1:])
    
    if direction == 'L':
        waypoint = np.roll(waypoint, -1 * value // 90)
    elif direction == 'R':
        waypoint = np.roll(waypoint, value // 90)
    elif direction == 'F':
        eastMove += value * waypoint[1] - value * waypoint[3]
        northMove += value * waypoint[0] - value * waypoint[2]
    
    if direction == 'N':
        waypoint[0] += value
    elif direction == 'S':
        waypoint[2] += value
    elif direction == 'W':
        waypoint[3] += value
    elif direction == 'E':
        waypoint[1] += value
    
print(abs(eastMove) + abs(northMove))