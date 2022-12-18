file1 = open('input.txt', 'r')
lines = file1.readlines()

cubes = set()
for line in [line.strip() for line in lines]:
    cubes.add(tuple([int(x) for x in line.split(',')]))

minval = -1
maxval = 25

outside = set()
outside.add((0,0,0))
queue = [(0,0,0)]
while len(queue) != 0:
    (x,y,z) = queue.pop(0)
    n = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
    for (i,j,k) in n:
        if minval <= i <= maxval and minval <= j <= maxval and minval <= k <= maxval and not (i,j,k) in outside and not (i,j,k) in cubes:
            outside.add((i,j,k))
            queue.append((i,j,k))

count = 0
for x,y,z in cubes:
    n = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
    for (i,j,k) in n:
        if (i,j,k) in outside:
            count += 1
print(count)