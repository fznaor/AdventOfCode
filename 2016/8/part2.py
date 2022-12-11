import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))
file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = np.empty((6,50), dtype=str)
mat[:,:] = ' '

for line in [line.strip() for line in lines]:
    if line.startswith('rect'):
        [x,y] = [int(x) for x in line.split(' ')[1].split('x')]
        mat[:y,:x] = '▮' 
    elif line.startswith('rotate column'):
        colIndex = int(line.split(' ')[2].split('=')[-1])
        rotBy = int(line.split(' ')[-1])
        mat[:,colIndex:colIndex+1] = np.roll(mat[:,colIndex:colIndex+1],rotBy)
    elif line.startswith('rotate row'):
        rowIndex = int(line.split(' ')[2].split('=')[-1])
        rotBy = int(line.split(' ')[-1])
        mat[rowIndex] = np.roll(mat[rowIndex], rotBy)
print(mat)