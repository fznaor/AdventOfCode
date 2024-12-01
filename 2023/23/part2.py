import numpy as np
import sys
sys.setrecursionlimit(50000)

file1 = open('input.txt', 'r')
lines = file1.readlines()

field = []

for line in [line.strip() for line in lines]:
    field.append([x for x in line])
field = np.matrix(field)

# build reduced map
checkpoints = {}
for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        if field[i,j] == '#':
            continue
        n = 0
        for ii,jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if ii < 0 or ii == field.shape[0] or jj < 0 or jj == field.shape[1]:
                continue
            if field[ii,jj] == '#':
                continue
            n += 1
        if n != 2:
            checkpoints[(i,j)] = []
for checkpoint in checkpoints:
    (ci,cj) = checkpoint
    dists = checkpoints[checkpoint]
    visited = set()
    visited.add((ci,cj))
    queue = [(visited, ci, cj, 0)]
    while len(queue) != 0:
        visited,i,j,d = queue.pop()
        notWalls = []
        for ii,jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if ii < 0 or ii == field.shape[0] or jj < 0 or jj == field.shape[1]:
                continue
            if field[ii,jj] == '#':
                continue
            notWalls.append((ii,jj))
        if len(notWalls) == 2 or (i,j) == (ci,cj):
            for (ii,jj) in notWalls:
                if (ii,jj) not in visited:
                    newVisited = visited.copy()
                    newVisited.add((ii,jj))
                    queue.append((newVisited,ii,jj,d+1))
        else:
            dists.append(((i,j),d))

longest = 0
queue = [(set(),0,1,0)]

while len(queue) != 0:
    visited,i,j,dist = queue.pop()

    for (ii,jj),d in checkpoints[(i,j)]:
        if (ii,jj) in visited:
            continue
        newVisited = visited.copy()
        newVisited.add((ii,jj))
        if ii == field.shape[0] - 1:
            if dist+d > longest:
                longest = dist+d
            continue
        queue.append((newVisited,ii,jj,dist+d))

print(longest)