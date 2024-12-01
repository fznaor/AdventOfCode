import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []

for line in [line.strip() for line in lines]:
    mat.append([x for x in line])
mat = np.matrix(mat)

s = 0
for j in range(0, mat.shape[1]):
    lastRock = -1
    for i in(range(0, mat.shape[0])):
        if mat[i,j] == '#':
            lastRock = i
        elif mat[i,j] == 'O':
            lastRock += 1
            s += mat.shape[0] - lastRock
print(s)