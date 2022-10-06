import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

cubes = []

def getOverlap(a,b):
    overlap = [max(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),min(a[3],b[3]),max(a[4],b[4]),min(a[5],b[5])]
    if overlap[0] > overlap[1] or overlap[2] > overlap[3] or overlap[4] > overlap[5]:
        return None
    else:
        return overlap
    
def getNonOverlap(a,b):
    res = []
    overlap = getOverlap(a,b)
    if overlap == None:
        res.append(a)
        return res
    if a[0] < overlap[0]:
        res.append([a[0], overlap[0]-1, a[2], a[3], a[4], a[5]])
    if a[1] > overlap[1]:
        res.append([overlap[1]+1, a[1], a[2], a[3], a[4], a[5]])
    if a[2] < overlap[2]:
        res.append([overlap[0], overlap[1], a[2], overlap[2]-1, a[4], a[5]])
    if a[3] > overlap[3]:
        res.append([overlap[0], overlap[1], overlap[3]+1, a[3], a[4], a[5]])
    if a[4] < overlap[4]:
        res.append([overlap[0], overlap[1], overlap[2], overlap[3], a[4], overlap[4]-1])
    if a[5] > overlap[5]:
        res.append([overlap[0], overlap[1], overlap[2], overlap[3], overlap[5]+1, a[5]])
    return res

for i,line in enumerate(lines):
    [command, coords] = line.rstrip().split(' ')
    [xCoords, yCoords, zCoords] = coords.split(',')
    [xLower, xUpper] = [int(a) for a in xCoords.split('=')[1].split('..')]
    [yLower, yUpper] = [int(a) for a in yCoords.split('=')[1].split('..')]
    [zLower, zUpper] = [int(a) for a in zCoords.split('=')[1].split('..')]
    
    if i == 0:
        cubes.append([xLower, xUpper, yLower, yUpper, zLower, zUpper])
        continue
    
    if command == 'on':
        newCubes = [[xLower, xUpper, yLower, yUpper, zLower, zUpper]]
        for cube in cubes:
            toDelete = []
            toAdd = []
            for j,newCube in enumerate(newCubes):
                nonOverlap = getNonOverlap(newCube, cube)
                if len(nonOverlap) > 0:
                    toAdd.extend(nonOverlap)
                if len(nonOverlap) > 0 or getOverlap(newCube, cube) != None:
                    toDelete.append(j)
            for j in range(len(toDelete)-1,-1,-1):
                del newCubes[toDelete[j]]
            newCubes.extend(toAdd)
        cubes.extend(newCubes)
    else:
        toAdd = []
        delCube = [xLower, xUpper, yLower, yUpper, zLower, zUpper]
        for cube in cubes:
            toAdd.extend(getNonOverlap(cube, delCube))
        cubes = toAdd

res = 0

for cube in cubes:
    res += (cube[1]-cube[0]+1) * (cube[3]-cube[2]+1) * (cube[5]-cube[4]+1)
print(res)
