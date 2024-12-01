import numpy as np
import sys
sys.setrecursionlimit(10000)

file1 = open('input.txt', 'r')
lines = file1.readlines()

field = []

for line in [line.strip() for line in lines]:
    field.append([x for x in line])
field = np.matrix(field)

longest = 0

def step(visited, i, j):
    global field, longest

    dirs = []
    if field[i,j] == '>':
        dirs.append((i,j+1))
    elif field[i,j] == '<':
        dirs.append((i,j-1))
    elif field[i,j] == 'v':
        dirs.append((i+1,j))
    elif field[i,j] == '^':
        dirs.append((i-1,j))
    else:
        dirs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

    for (ii,jj) in dirs:
        if (ii,jj) in visited:
            continue
        if ii < 0 or ii == field.shape[0] or jj < 0 or jj == field.shape[1]:
            continue
        if field[ii,jj] == '#':
            continue
        newVisited = visited.copy()
        newVisited.add((ii,jj))
        if ii == field.shape[0] - 1:
            if len(newVisited) > longest:
                longest = len(newVisited)
            return
        step(newVisited,ii,jj)

step(set(), 0, 1)
print(longest)