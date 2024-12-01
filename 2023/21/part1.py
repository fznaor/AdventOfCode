import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

field = []

for line in [line.strip() for line in lines]:
    field.append([x for x in line])
field = np.matrix(field)

sx,sy = (np.where(field=='S')[0][0]), (np.where(field=='S')[1][0])

positions = set()
positions.add((sx,sy))
for i in range(64):
    newPos = set()
    for (x,y) in positions:
        for (xx,yy) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if xx < 0 or xx == field.shape[0] or y < 0 or y == field.shape[1]:
                continue
            if field[xx,yy] == '.' or field[xx,yy] == 'S':
                newPos.add((xx,yy))
    positions = newPos
print(len(positions))