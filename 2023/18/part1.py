import numpy as np
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

boundary = []
boundary.append((0,0))
inbetweeners = 0

i,j = 0,0
for line in [line.strip() for line in lines]:
    dir = line.split()[0]
    steps = int(line.split()[1])

    if dir == 'U':
        i -= steps
    if dir == 'D':
        i += steps
    if dir == 'L':
        j -= steps
    if dir == 'R':
        j += steps
    
    inbetweeners += steps - 1
    boundary.append((i,j))

area = 0
for (x1,y1),(x2,y2) in zip(boundary[:-1], boundary[1:]):
    area += (y1+y2)*(x1-x2)
area *= 0.5
area = abs(area)
x = len(boundary) - 1 + inbetweeners
print(int(area - x/2 + 1 + x))