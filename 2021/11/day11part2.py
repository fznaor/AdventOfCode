import numpy as np

file1 = open('v21.txt', 'r')
lines = file1.readlines()

mat = [[int(digit) for digit in line.rstrip()] for line in lines]
mat = np.array(mat)
mat = np.pad(mat, pad_width=1, mode='constant', constant_values=-1)

def flash(i,j):
    global hasFlashed
    if hasFlashed[i][j]:
        return
    if mat[i-1][j] != -1:
        mat[i-1][j] += 1
        if mat[i-1][j] == 10:
            flash(i-1, j)
    if mat[i-1][j-1] != -1:
        mat[i-1][j-1] += 1
        if mat[i-1][j-1] == 10:
            flash(i-1, j-1)
    if mat[i+1][j] != -1:
        mat[i+1][j] += 1
        if mat[i+1][j] == 10:
            flash(i+1, j)
    if mat[i+1][j-1] != -1:
        mat[i+1][j-1] += 1
        if mat[i+1][j-1] == 10:
            flash(i+1, j-1)
    if mat[i+1][j+1] != -1:
        mat[i+1][j+1] += 1
        if mat[i+1][j+1] == 10:
            flash(i+1, j+1)
    if mat[i-1][j+1] != -1:
        mat[i-1][j+1] += 1
        if mat[i-1][j+1] == 10:
            flash(i-1, j+1)
    if mat[i][j+1] != -1:
        mat[i][j+1] += 1
        if mat[i][j+1] == 10:
            flash(i, j+1)
    if mat[i][j-1] != -1:
        mat[i][j-1] += 1
        if mat[i][j-1] == 10:
            flash(i, j-1)
    hasFlashed[i][j] = True

i=1
while(True):
    hasFlashed = np.zeros((len(mat), len(mat)), dtype='bool')
    mat[mat != -1] += 1
    for j in range(1, len(mat)-1):
        for k in range(1, len(mat)-1):
            if mat[j][k] != -1 and mat[j][k] >= 10:
                flash(j,k)
    if (mat >= 10).sum() == pow(len(mat)-2,2):
        print(i)
        break
    mat[mat >= 10] = 0
    i+=1
