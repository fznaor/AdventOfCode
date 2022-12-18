file1 = open('input.txt', 'r')
lines = file1.readlines()

cubes = set()
for line in [line.strip() for line in lines]:
    cubes.add(tuple([int(x) for x in line.split(',')]))

count = 0
for x,y,z in cubes:
    n = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
    for (i,j,k) in n:
        if not (i,j,k) in cubes:
            count += 1
print(count)