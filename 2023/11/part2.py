import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []
for line in [line.strip() for line in lines]:
    arr.append([x for x in line])
arr = np.matrix(arr)

emptyRows = []
emptyCols = []
for i in range(len(arr)):
    count = np.count_nonzero(arr[i] == '#')
    if count == 0:
        emptyRows.append(i)
for i in range(arr.shape[1]):
    count = np.count_nonzero(arr[:,i] == '#')
    if count == 0:
        emptyCols.append(i)

s = 0
galaxies = np.argwhere(arr == '#')
for i, (x1,y1) in enumerate(galaxies):
    for j in range(i+1, len(galaxies)):
        (x2,y2) = galaxies[j]
        s += abs(x2-x1) + abs(y2-y1)
        s += 999999 * len(list(set(emptyRows).intersection(range(x1 if x1 < x2 else x2,x2 if x1 < x2 else x1))))
        s += 999999 * len(list(set(emptyCols).intersection(range(y1 if y1 < y2 else y2,y2 if y1 < y2 else y1))))
print(s)