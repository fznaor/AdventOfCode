import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []
seen = []

for line in [line.strip() for line in lines]:
    mat.append([x for x in line])
mat = np.matrix(mat)

seen.append(mat.tolist())

for cycle in range(1,1000000000):
    for x in range(4):
        for j in range(0, mat.shape[1]):
            lastRock = -1
            for i in(range(0, mat.shape[0])):
                if mat[i,j] == '#':
                    lastRock = i
                elif mat[i,j] == 'O':
                    lastRock += 1
                    mat[lastRock,j] = 'O'
                    if lastRock != i:
                        mat[i,j] = '.'
        mat = np.rot90(mat, k = -1)
    if mat.tolist() in seen:
        cycleStart = seen.index(mat.tolist())
        seen = seen[cycleStart:]
        mat = np.matrix(seen[(1000000000) % (cycle - cycleStart) - cycleStart])
        break
    seen.append(mat.tolist())
            
s = 0
for j in range(0, mat.shape[1]):
    lastRock = -1
    for i in(range(0, mat.shape[0])):
        if mat[i,j] == 'O':
            s += mat.shape[0] - i
print(s)