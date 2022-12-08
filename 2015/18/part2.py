file1 = open('input.txt', 'r')
lines = file1.readlines()
import numpy as np

arr = []
DIM = len(lines)
for line in [line.strip() for line in lines]:
    arr.append([x for x in line])
arr = np.matrix(arr)
arr[0, DIM-1] = '#'
arr[DIM-1, DIM-1] = '#'
arr[0, 0] = '#'
arr[DIM-1, 0] = '#'

for step in range(100):
    newArr = arr.copy()
    for i in range(DIM):
        for j in range(DIM):
            if (i,j) in [(0,DIM-1), (DIM-1,DIM-1), (0,0), (DIM-1,0)]:
                continue
            onNeighbours = 0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ii < 0 or ii >= DIM or jj < 0 or jj >= DIM or (i == ii and j == jj):
                        continue
                    elif arr[ii,jj] == '#':
                        onNeighbours += 1
            if arr[i,j] == '#' and not onNeighbours in [2,3]:
                newArr[i,j] = '.'
            elif onNeighbours == 3:
                newArr[i,j] = '#'
    arr = newArr
print(np.count_nonzero(arr == '#'))