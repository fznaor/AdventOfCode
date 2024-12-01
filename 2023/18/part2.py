file1 = open('input.txt', 'r')
lines = file1.readlines()

boundary = []
boundary.append((0,0))
inbetweeners = 0

i,j = 0,0
for line in [line.strip() for line in lines]:
    val = line.split('(')[1][:-1]
    
    steps = int(val[1:-1], 16)
    dir = int(val[-1])

    if dir == 3:
        i -= steps
    if dir == 1:
        i += steps
    if dir == 2:
        j -= steps
    if dir == 0:
        j += steps
    
    boundary.append((i,j))
    inbetweeners += steps - 1

area = 0
for (x1,y1),(x2,y2) in zip(boundary[:-1], boundary[1:]):
    area += (y1+y2)*(x1-x2)
area *= 0.5
area = abs(area)
x = len(boundary) - 1 + inbetweeners
print(int(area - x/2 + 1 + x))