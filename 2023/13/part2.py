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
        if (mat[i,:] == mat[i+1,:]).all() or np.count_nonzero((mat[i,:] == mat[i+1,:]) == False) == 1:
            i1 = i-1
            i2 = i+2
            valid = True
            smudgeFound = False
            if np.count_nonzero((mat[i,:] == mat[i+1,:]) == False) == 1:
                smudgeFound = True
            while i1 >= 0 and i2 < mat.shape[0]:
                if np.count_nonzero((mat[i1,:] == mat[i2,:]) == False) == 1:
                    if smudgeFound:
                        valid = False
                        break
                    else:
                        smudgeFound = True
                elif not (mat[i1,:] == mat[i2,:]).all():
                    valid = False
                    break
                i1 -= 1
                i2 += 1
            if valid and smudgeFound:
                foundInRows = True
                s += 100 * (i + 1)
                break
    if foundInRows:
        continue
    for j in range(mat.shape[1]-1):
        if (mat[:,j] == mat[:,j+1]).all() or np.count_nonzero((mat[:,j] == mat[:,j+1]) == False) == 1:
            j1 = j-1
            j2 = j+2
            valid = True
            smudgeFound = False
            if np.count_nonzero((mat[:,j] == mat[:,j+1]) == False) == 1:
                smudgeFound = True
            while j1 >= 0 and j2 < mat.shape[1]:
                if np.count_nonzero((mat[:,j1] == mat[:,j2]) == False) == 1:
                    if smudgeFound:
                        valid = False
                        break
                    else:
                        smudgeFound = True
                elif not (mat[:,j1] == mat[:,j2]).all():
                    valid = False
                    break
                j1 -= 1
                j2 += 1
            if valid and smudgeFound:
                s += j + 1
                break
print(s)