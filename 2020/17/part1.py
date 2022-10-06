file1 = open('input.txt', 'r')
lines = file1.readlines()

active = []

def countActiveNeighbours(x,y,z):
    res = 0
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                if (i,j,k) != (x,y,z):
                    if [i,j,k] in active:
                        res += 1
    return res

for i,line in enumerate(lines):
    for j,sign in enumerate(line.rstrip()):
        if sign == '#':
            active.append([i,j,0])
            
for iters in range(6):
    newActive = []
    for el in active:
        [x,y,z] = el
        if countActiveNeighbours(x,y,z) in [2,3]:
            newActive.append(el)
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                for k in [z-1, z, z+1]:
                    if (i,j,k) != (x,y,z):
                        if [i,j,k] not in active and [i,j,k] not in newActive:
                            if countActiveNeighbours(i,j,k) == 3:
                                newActive.append([i,j,k])
    active = newActive
    
print(len(active))