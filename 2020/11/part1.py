import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

seats = []

for line in lines:
    seats.append([c for c in line.rstrip()])
    
seats = np.array(seats)
seats = np.pad(seats, pad_width=1, mode='constant', constant_values='~')

def countNeighbours(i,j,occupied):
    target = '#' if occupied else 'L'
    suma = 0
    if seats[i-1][j] == target:
        suma += 1
    if seats[i-1][j-1] == target:
        suma += 1
    if seats[i-1][j+1] == target:
        suma += 1
    if seats[i+1][j] == target:
        suma += 1
    if seats[i+1][j+1] == target:
        suma += 1
    if seats[i+1][j-1] == target:
        suma += 1
    if seats[i][j-1] == target:
        suma += 1
    if seats[i][j+1] == target:
        suma += 1
    return suma
        
while True:
    changeToEmpty = []
    changeToOccupied = []
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            if seats[i][j] == 'L' and countNeighbours(i,j,True) == 0:
                changeToOccupied.append((i,j))
            elif seats[i][j] == '#' and countNeighbours(i,j,True) >= 4:
                changeToEmpty.append((i,j))
    for (i,j) in changeToEmpty:
        seats[i][j] = 'L'
    for (i,j) in changeToOccupied:
        seats[i][j] = '#'
    if len(changeToEmpty) == 0 and len(changeToOccupied) == 0:
        print(np.sum(seats == '#'))
        break