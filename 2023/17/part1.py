import numpy as np
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

field = []

for line in [line.strip() for line in lines]:
    field.append([int(x) for x in line])
field = np.matrix(field)

dist = {}
nonVisited = set()

dist[(0,0,'R',0)] = 0
nonVisited.add((0,0,'R',0))

while True:
    minDist = math.inf
    minx = math.inf
    miny = math.inf
    mindir = ''
    minstreak = math.inf

    for (x,y,dir,streak) in nonVisited:
        if dist[(x,y,dir,streak)] < minDist:
            minDist = dist[(x,y,dir,streak)]
            minx, miny, mindir, minstreak = x,y,dir,streak

    nonVisited.remove((minx,miny,mindir,minstreak))

    if minx == field.shape[0] - 1 and miny == field.shape[1] - 1:
        print(minDist)
        break
    
    if mindir == 'R':
        if miny + 1 < field.shape[1] and minstreak < 3:
            if not (minx, miny+1, 'R', minstreak+1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx,miny+1] < dist[(minx, miny+1, 'R', minstreak+1)]:
                dist[(minx, miny+1, 'R', minstreak+1)] = dist[(minx, miny, mindir, minstreak)] + field[minx,miny+1]
                nonVisited.add((minx,miny+1,'R',minstreak+1))
    if mindir == 'L':
        if miny - 1 >= 0 and minstreak < 3:
            if not (minx, miny-1, 'L', minstreak+1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx,miny-1] < dist[(minx, miny-1, 'L', minstreak+1)]:
                dist[(minx, miny-1, 'L', minstreak+1)] = dist[(minx, miny, mindir, minstreak)] + field[minx,miny-1]
                nonVisited.add((minx,miny-1,'L',minstreak+1))
    if mindir == 'D':
        if minx + 1 < field.shape[0] and minstreak < 3:
            if not (minx+1, miny, 'D', minstreak+1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx+1,miny] < dist[(minx+1, miny, 'D', minstreak+1)]:
                dist[(minx+1, miny, 'D', minstreak+1)] = dist[(minx, miny, mindir, minstreak)] + field[minx+1,miny]
                nonVisited.add((minx+1,miny,'D',minstreak+1))
    if mindir == 'U':
        if minx - 1 >= 0 and minstreak < 3:
            if not (minx-1, miny, 'U', minstreak+1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx-1,miny] < dist[(minx-1, miny, 'U', minstreak+1)]:
                dist[(minx-1, miny, 'U', minstreak+1)] = dist[(minx, miny, mindir, minstreak)] + field[minx-1,miny]
                nonVisited.add((minx-1,miny,'U',minstreak+1))

    if mindir != 'R' and mindir != 'L':
        if miny + 1 < field.shape[1]:
            if not (minx, miny+1, 'R', 1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx,miny+1] < dist[(minx, miny+1, 'R', 1)]:
                dist[(minx, miny+1, 'R', 1)] = dist[(minx, miny, mindir, minstreak)] + field[minx,miny+1]
                nonVisited.add((minx,miny+1,'R',1))
    if mindir != 'L' and mindir != 'R':
        if miny - 1 >= 0:
            if not (minx, miny-1, 'L', 1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx,miny-1] < dist[(minx, miny-1, 'L', 1)]:
                dist[(minx, miny-1, 'L', 1)] = dist[(minx, miny, mindir, minstreak)] + field[minx,miny-1]
                nonVisited.add((minx,miny-1,'L',1))
    if mindir != 'D' and mindir != 'U':
        if minx + 1 < field.shape[0]:
            if not (minx+1, miny, 'D', 1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx+1,miny] < dist[(minx+1, miny, 'D', 1)]:
                dist[(minx+1, miny, 'D', 1)] = dist[(minx, miny, mindir, minstreak)] + field[minx+1,miny]
                nonVisited.add((minx+1,miny,'D',1))
    if mindir != 'U' and mindir != 'D':
        if minx - 1 >= 0:
            if not (minx-1, miny, 'U', 1) in dist or dist[(minx, miny, mindir, minstreak)] + field[minx-1,miny] < dist[(minx-1, miny, 'U', 1)]:
                dist[(minx-1, miny, 'U', 1)] = dist[(minx, miny, mindir, minstreak)] + field[minx-1,miny]
                nonVisited.add((minx-1,miny,'U',1))
