import numpy as np

file1 = open('v21.txt', 'r')
lines = file1.readlines()

inputs = lines[0].rstrip().split(',')
inputs = [int(x) for x in inputs]

inputs = np.sort(inputs)
best = -1

for i in range(inputs[0],inputs[-1]):
    suma = 0
    for j in inputs:
        suma += (abs(i-j)*(abs(i-j)+1))/2
    if best == -1:
        best = suma
    elif suma < best:
        best = suma
        
print(best)