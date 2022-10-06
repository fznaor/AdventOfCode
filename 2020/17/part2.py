file1 = open('input.txt', 'r')
lines = file1.readlines()

active = []

def countActiveNeighbours(x,y,z,w):
    res = 0
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                for l in [w-1, w, w+1]:
                    if (i,j,k,l) != (x,y,z,w):
                        if [i,j,k,l] in active:
                            res += 1
                            if res == 4:
                                return res
    return res

for i,line in enumerate(lines):
    for j,sign in enumerate(line.rstrip()):
        if sign == '#':
            active.append([i,j,0,0])
            
for iters in range(6):
    newActive = []
    for el in active:
        [x,y,z,w] = el
        if countActiveNeighbours(x,y,z,w) in [2,3]:
            newActive.append(el)
        for i in [x-1, x, x+1]:
            for j in [y-1, y, y+1]:
                for k in [z-1, z, z+1]:
                    for l in [w-1, w, w+1]:
                        if (i,j,k,l) != (x,y,z,w):
                            if [i,j,k,l] not in active and [i,j,k,l] not in newActive:
                                if countActiveNeighbours(i,j,k,l) == 3:
                                    newActive.append([i,j,k,l])
    active = newActive
    
print(len(active))