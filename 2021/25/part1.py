import numpy as np
import copy

file1 = open('input.txt', 'r')
lines = file1.readlines()

for i,line in enumerate(lines):
    
    if i == 0:
        arr = np.empty([0, len(line.rstrip())])
        row = [x for x in line.rstrip()]
        arr = np.vstack([arr, row])
        
    else:
        row = [x for x in line.rstrip()]
        arr = np.vstack([arr, row])
        
iters = 0

while True:
    iters += 1
    hasChanged = False
    arrC = copy.deepcopy(arr)
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if j == arr.shape[1] - 1:
                if arr[i][0] == '.' and arr[i][j] == '>':
                    arrC[i][0] = '>'
                    arrC[i][j] = '.'
                    hasChanged = True
            else:
                if arr[i][j] == '>' and arr[i][j+1] == '.':
                    arrC[i][j] = '.'
                    arrC[i][j+1] = '>'
                    hasChanged = True
                    
    arr = copy.deepcopy(arrC)
                    
    for j in range(arr.shape[1]):
        for i in range(arr.shape[0]):
            if i == arr.shape[0] - 1:
                if arr[0][j] == '.' and arr[i][j] == 'v':
                    arrC[0][j] = 'v'
                    arrC[i][j] = '.'
                    hasChanged = True
            else:
                if arr[i][j] == 'v' and arr[i+1][j] == '.':
                    arrC[i][j] = '.'
                    arrC[i+1][j] = 'v'
                    hasChanged = True
        
    arr = copy.deepcopy(arrC)
    
    if not hasChanged:
        print(iters)
        break
