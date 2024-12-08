import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []

for line in [line.strip() for line in lines]:
    mat.append([x for x in line])

mat = np.array(mat)
nRows, nColumns = np.shape(mat)
uniqueVals = np.unique(mat)

antinodes = set()

for val in uniqueVals:
    if val == '.':
        continue
    indices = np.where(mat == val)
    positions = list(zip(indices[0], indices[1]))
    for x,y in positions:
        for w,z in positions:
            if(x == w and y == z):
                continue
            anx = x - (w - x)
            any = y - (z - y)
            if anx in range(nRows) and any in range(nColumns):
                antinodes.add((anx,any))

print(len(antinodes))