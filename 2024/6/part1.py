import numpy as np

def isInBounds(x, y, nRows, nColumns):
    return x >= 0 and x < nRows and y >= 0 and y < nColumns

def rotate(dir):
    if dir == 'N':
        return 'E'
    if dir == 'E':
        return 'S'
    if dir == 'S':
        return 'W'
    return 'N'

def getNewPos(x, y, dir):
    if dir == 'N':
        return (x-1,y)
    if dir == 'E':
        return (x,y+1)
    if dir == 'S':
        return (x+1,y)
    return (x,y-1)

file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []

for line in [line.strip() for line in lines]:
    mat.append([x for x in line])

mat = np.mat(mat)
nRows, nColumns = np.shape(mat)
x, y = [x[0] for x in np.where(mat == '^')]
dir = 'N'
visited = set()

while True:
    if not isInBounds(x, y, nRows, nColumns):
        break
    visited.add((x,y))
    if dir == 'N':
        if isInBounds(x-1,y,nRows,nColumns) and mat[x-1, y] == '#':
            dir = rotate(dir)
    elif isInBounds(x+1,y,nRows,nColumns) and dir == 'S':
        if mat[x+1, y] == '#':
            dir = rotate(dir)
    elif isInBounds(x,y-1,nRows,nColumns) and dir == 'W':
        if mat[x, y-1] == '#':
            dir = rotate(dir)
    elif isInBounds(x,y+1,nRows,nColumns) and dir == 'E':
        if mat[x, y+1] == '#':
            dir = rotate(dir)
    x,y = getNewPos(x,y,dir)
print(len(visited))