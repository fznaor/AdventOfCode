import numpy as np
import sys
sys.setrecursionlimit(5500)

file1 = open('input.txt', 'r')
lines = file1.readlines()

field = []

for line in [line.strip() for line in lines]:
    field.append([x for x in line])
field = np.matrix(field)
fieldVisited = np.zeros(field.shape, bool)
visitedDirs = []

def move(i,j,dir):
    global field, fieldVisited, visitedDirs

    if i < 0 or i >= field.shape[0] or j < 0 or j >= field.shape[1]:
        return
    if (i,j,dir) in visitedDirs:
        return
    visitedDirs.append((i,j,dir))
    fieldVisited[i,j] = True
    
    currField = field[i,j]
    if dir == 'R':
        if currField == '.' or currField == '-':
            move(i,j+1,'R')
        if currField == '/':
            move(i-1,j,'U')
        if currField == '\\':
            move(i+1,j,'D')
        if currField == '|':
            move(i-1,j,'U')
            move(i+1,j,'D')
    
    if dir == 'L':
        if currField == '.' or currField == '-':
            move(i,j-1,'L')
        if currField == '/':
            move(i+1,j,'D')
        if currField == '\\':
            move(i-1,j,'U')
        if currField == '|':
            move(i-1,j,'U')
            move(i+1,j,'D')

    if dir == 'U':
        if currField == '.' or currField == '|':
            move(i-1,j,'U')
        if currField == '/':
            move(i,j+1,'R')
        if currField == '\\':
            move(i,j-1,'L')
        if currField == '-':
            move(i,j+1,'R')
            move(i,j-1,'L')

    if dir == 'D':
        if currField == '.' or currField == '|':
            move(i+1,j,'D')
        if currField == '/':
            move(i,j-1,'L')
        if currField == '\\':
            move(i,j+1,'R')
        if currField == '-':
            move(i,j+1,'R')
            move(i,j-1,'L')

maxS = 0
for i in range(field.shape[0]):
    move(i,0,'R')
    if np.count_nonzero(fieldVisited == True) > maxS:
        maxS = np.count_nonzero(fieldVisited == True)
    fieldVisited = np.zeros(field.shape, bool)
    visitedDirs = []

    move(i,field.shape[1]-1,'L')
    if np.count_nonzero(fieldVisited == True) > maxS:
        maxS = np.count_nonzero(fieldVisited == True)
    fieldVisited = np.zeros(field.shape, bool)
    visitedDirs = []
for j in range(field.shape[1]):
    move(0,j,'D')
    if np.count_nonzero(fieldVisited == True) > maxS:
        maxS = np.count_nonzero(fieldVisited == True)
    fieldVisited = np.zeros(field.shape, bool)
    visitedDirs = []

    move(field.shape[0]-1,j,'U')
    if np.count_nonzero(fieldVisited == True) > maxS:
        maxS = np.count_nonzero(fieldVisited == True)
    fieldVisited = np.zeros(field.shape, bool)
    visitedDirs = []
print(maxS)