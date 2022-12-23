file1 = open('input.txt', 'r')
lines = file1.readlines()
import math

elves = []

for i,line in enumerate([line.strip() for line in lines]):
    for j,x in enumerate(line):
        if x == '#':
            elves.append((i,j)) 

dirs = ['n','s','w','e']
for i in range(10):
    proposals = dict()
    elveProposals = []
    for (x,y) in elves:
        found = False
        emptyNeighbours = 0
        for (a,b) in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
            if not (a,b) in elves:
                emptyNeighbours += 1
        if emptyNeighbours != 8:
            for d in dirs:
                if d == 'n':
                    if (not (x-1,y-1) in elves) and (not (x-1,y) in elves) and (not (x-1,y+1) in elves):
                        elveProposals.append((x-1,y))
                        found = True
                        if not (x-1,y) in proposals:
                            proposals[(x-1,y)] = 1
                        else:
                            proposals[(x-1,y)] += 1
                        break
                elif d == 's':
                    if (not (x+1,y-1) in elves) and (not (x+1,y) in elves) and (not (x+1,y+1) in elves):
                        elveProposals.append((x+1,y))
                        found = True
                        if not (x+1,y) in proposals:
                            proposals[(x+1,y)] = 1
                        else:
                            proposals[(x+1,y)] += 1
                        break
                elif d == 'w':
                    if (not (x-1,y-1) in elves) and (not (x,y-1) in elves) and (not (x+1,y-1) in elves):
                        elveProposals.append((x,y-1))
                        found = True
                        if not (x,y-1) in proposals:
                            proposals[(x,y-1)] = 1
                        else:
                            proposals[(x,y-1)] += 1
                        break
                elif d == 'e':
                    if (not (x-1,y+1) in elves) and (not (x,y+1) in elves) and (not (x+1,y+1) in elves):
                        elveProposals.append((x,y+1))
                        found = True
                        if not (x,y+1) in proposals:
                            proposals[(x,y+1)] = 1
                        else:
                            proposals[(x,y+1)] += 1
                        break
        if not found:
            elveProposals.append((x,y))
            proposals[(x,y)] = 1
    
    newElves = []
    for i,(x,y) in enumerate(elves):
        xp,yp = elveProposals[i]
        if proposals[(xp,yp)] < 2:
            newElves.append((xp,yp))
        else:
            newElves.append((x,y))
    elves = newElves
            
    dirs = dirs[1:] + [dirs[0]]
    
maxx,maxy,minx,miny = -math.inf,-math.inf,math.inf,math.inf
for (x,y) in elves:
    if x > maxx:
        maxx = x
    if x < minx:
        minx = x
    if y > maxy:
        maxy = y
    if y < miny:
        miny = y
        
print((maxx-minx+1)*(maxy-miny+1) - len(elves))