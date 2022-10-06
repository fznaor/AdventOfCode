import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

seats = []

for line in lines:
    seats.append([c for c in line.rstrip()])
    
seats = np.array(seats)
seats = np.pad(seats, pad_width=1, mode='constant', constant_values='~')

def countVisibleOccupied(i,j):
    suma = 0
    for ii in range(i-1, -1, -1):
        if seats[ii][j] == '#':
            suma += 1
            break
        elif seats[ii][j] == 'L':
            break
    for ii in range(i+1,seats.shape[0]):
        if seats[ii][j] == '#':
            suma += 1
            break
        elif seats[ii][j] == 'L':
            break
    for jj in range(j-1, -1, -1):
        if seats[i][jj] == '#':
            suma += 1
            break
        elif seats[i][jj] == 'L':
            break
    for jj in range(j+1,seats.shape[1]):
        if seats[i][jj] == '#':
            suma += 1
            break
        elif seats[i][jj] == 'L':
            break
    ii = i+1
    jj = j+1
    while not (ii < 0 or ii >= seats.shape[0] or jj < 0 or jj >= seats.shape[1]):
        if seats[ii][jj] == '#':
            suma += 1
            break
        elif seats[ii][jj] == 'L':
            break
        ii += 1
        jj += 1
    ii = i+1
    jj = j-1
    while not (ii < 0 or ii >= seats.shape[0] or jj < 0 or jj >= seats.shape[1]):
        if seats[ii][jj] == '#':
            suma += 1
            break
        elif seats[ii][jj] == 'L':
            break
        ii += 1
        jj -= 1
    ii = i-1
    jj = j+1
    while not (ii < 0 or ii >= seats.shape[0] or jj < 0 or jj >= seats.shape[1]):
        if seats[ii][jj] == '#':
            suma += 1
            break
        elif seats[ii][jj] == 'L':
            break
        ii -= 1
        jj += 1
    ii = i-1
    jj = j-1
    while not (ii < 0 or ii >= seats.shape[0] or jj < 0 or jj >= seats.shape[1]):
        if seats[ii][jj] == '#':
            suma += 1
            break
        elif seats[ii][jj] == 'L':
            break
        ii -= 1
        jj -= 1
    return suma
        
while True:
    changeToEmpty = []
    changeToOccupied = []
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            if seats[i][j] == 'L' and countVisibleOccupied(i,j) == 0:
                changeToOccupied.append((i,j))
            elif seats[i][j] == '#' and countVisibleOccupied(i,j) >= 5:
                changeToEmpty.append((i,j))
    for (i,j) in changeToEmpty:
        seats[i][j] = 'L'
    for (i,j) in changeToOccupied:
        seats[i][j] = '#'
    if len(changeToEmpty) == 0 and len(changeToOccupied) == 0:
        print(np.sum(seats == '#'))
        break