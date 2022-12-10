file1 = open('input.txt', 'r')
lines = file1.readlines()
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

board = np.empty([240], dtype = str)

cycle = 0
x = 1
res = 0
for line in [line.strip().split(' ') for line in lines]:
    if line[0] == "noop":
        cycle += 1
        if (cycle-1) % 40 in range(x-1,x+2):
            board[cycle-1] = '#'
        else:
            board[cycle-1] = '.'
    else:
        cycle += 1
        if (cycle-1) % 40 in range(x-1,x+2):
            board[cycle-1] = '#'
        else:
            board[cycle-1] = '.'
        cycle += 1
        if (cycle-1) % 40 in range(x-1,x+2):
            board[cycle-1] = '#'
        else:
            board[cycle-1] = '.'
        x += int(line[1])
print(np.reshape(board, [6,40]))