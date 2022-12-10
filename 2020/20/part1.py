import numpy as np
file1 = open('input.txt', 'r')
lines = file1.readlines()

def countEquals(mat1, mat2):
    arr1 = [np.ravel(mat1[0,:]), 
            np.ravel(mat1[-1,:]), 
            np.ravel(mat1[:,0]),
            np.ravel(mat1[:,-1])]
    
    arr2 = [np.ravel(mat2[0,:]), np.ravel(mat2[0,::-1]),
            np.ravel(mat2[-1,:]), np.ravel(mat2[-1,::-1]),
            np.ravel(mat2[:,0]), np.ravel(mat2[::-1,0]),
            np.ravel(mat2[:,-1]), np.ravel(mat2[::-1,-1])]
    
    for a1 in arr1:
        for a2 in arr2:
            if np.array_equal(a1, a2):
                return True
    return False

mats = dict()

for i,line in enumerate(lines):
    if i % 12 == 0:
        currIndex = int(line.strip().split(' ')[1].split(':')[0])
    elif i % 12 == 1:
        arr = [list(line.strip())]
    elif 1 < (i % 12) < 10:
        arr.append(list(line.strip()))
    elif i % 12 == 10:
        arr.append(list(line.strip()))
        mats[currIndex] = np.matrix(arr)

res = 1
for i in mats:
    count = 0
    for j in mats:
        if i==j:
            continue
        if countEquals(mats[i], mats[j]) :
            count += 1
    if count == 2:
        res *= i
print(res)
            