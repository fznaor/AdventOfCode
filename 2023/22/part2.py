import copy

file1 = open('input.txt', 'r')
lines = file1.readlines()

cubes = []

for line in [line.strip() for line in lines]:
    part1 = tuple([int(x) for x in line.split('~')[0].split(',')])
    part2 = tuple([int(x) for x in line.split('~')[1].split(',')])
    cubes.append((part1,part2))

#falling cubes
while True:
    cubesMoved = False
    for i in range(len(cubes)):
        hiZ = 1
        (c1sx,c1sy,c1sz),(c1ex,c1ey,c1ez) = cubes[i]
        for j in range(len(cubes)):
            if i == j:
                continue

            (c2sx,c2sy,c2sz),(c2ex,c2ey,c2ez) = cubes[j]
            if (max(c1sx,c2sx) <= min(c1ex,c2ex)) and (max(c1sy,c2sy) <= min(c1ey,c2ey)) and c1sz > c2ez:
                if c2ez + 1 > hiZ:
                    hiZ = c2ez + 1
        if hiZ != c1sz:
            cubesMoved = True
            diff = c1sz - hiZ
            c1sz -= diff
            c1ez -= diff
            cubes[i] = ((c1sx,c1sy,c1sz),(c1ex,c1ey,c1ez))
    if not cubesMoved:
        break

supports = {}
for i in range(len(cubes)):
    supportingCubes = []
    (c1sx,c1sy,c1sz),(c1ex,c1ey,c1ez) = cubes[i]
    for j in range(len(cubes)):
        if i == j:
            continue
        (c2sx,c2sy,c2sz),(c2ex,c2ey,c2ez) = cubes[j]

        if (max(c1sx,c2sx) <= min(c1ex,c2ex)) and (max(c1sy,c2sy) <= min(c1ey,c2ey)) and c1sz == c2ez + 1:
            supportingCubes.append(j)
    supports[i] = supportingCubes

deletions = 0
for cubeIndex in supports:
    tempSupports = copy.deepcopy(supports)
    toDelete = [cubeIndex]
    while len(toDelete) > 0:
        currentlyDeleting = toDelete.pop()
        for cube in tempSupports:
            if cube == cubeIndex:
                continue
            elif currentlyDeleting in tempSupports[cube]:
                tempSupports[cube].remove(currentlyDeleting)
                if len(tempSupports[cube]) == 0:
                    toDelete.append(cube)
                    deletions +=1
print(deletions)