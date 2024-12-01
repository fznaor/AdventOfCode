import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

mats = []
currMat = []
for line in [line.strip() for line in lines]:
    if len(line) == 0:
        mats.append(currMat.copy())
        currMat = []
    else:
        currMat.append([x for x in line])
mats.append(currMat)

s = 0
for mat in mats:
    mat = np.matrix(mat)
    foundInRows = False
    for i in range(mat.shape[0]-1):
        if (mat[i,:] == mat[i+1,:]).all():
            i1 = i-1
            i2 = i+2
            valid = True
            while i1 >= 0 and i2 < mat.shape[0]:
                if not (mat[i1,:] == mat[i2,:]).all():
                    valid = False
                    break
                i1 -= 1
                i2 += 1
            if valid:
                foundInRows = True
                s += 100 * (i + 1)
                break
    if foundInRows:
        continue
    for j in range(mat.shape[1]-1):
        if (mat[:,j] == mat[:,j+1]).all():
            j1 = j-1
            j2 = j+2
            valid = True
            while j1 >= 0 and j2 < mat.shape[1]:
                if not (mat[:,j1] == mat[:,j2]).all():
                    valid = False
                    break
                j1 -= 1
                j2 += 1
            if valid:
                s += j + 1
                break
print(s)