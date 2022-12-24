file1 = open('input.txt', 'r')
lines = file1.readlines()
import math

walls = set()
ub = set()
db = set()
lb = set()
rb= set()
height = len(lines)
width = len(lines[0].strip())

for i,line in enumerate([line.strip() for line in lines]):
    for j,x in enumerate(line):
        if i == 0 and x == '.':
            start = (i,j)
        elif x == '.':
            finish = (i,j)
        elif x == '#':
            walls.add((i,j))
        elif x == '<':
            lb.add((i,j))
        elif x == '>':
            rb.add((i,j))
        elif x == '^':
            ub.add((i,j))
        elif x == 'v':
            db.add((i,j))

moveCount = 0
positions = set()
positions.add(start)
found = False
while True:
    moveCount += 1
    nub,ndb,nlb,nrb = set(),set(),set(),set()
    for (x,y) in ub:
        if x >= 2:
            nub.add((x-1,y))
        else:
            nub.add((height-2,y))
    for (x,y) in db:
        if x <= height-3:
            ndb.add((x+1,y))
        else:
            ndb.add((1,y))
    for (x,y) in lb:
        if y >= 2:
            nlb.add((x,y-1))
        else:
            nlb.add((x,width-2))
    for (x,y) in rb:
        if y <= width-3:
            nrb.add((x,y+1))
        else:
            nrb.add((x,1))
    
    newPos = set()
    for(x,y) in positions:
        for (nx,ny) in [(x,y),(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
            if (nx,ny) in walls or nx < 0:
                continue
            if (nx,ny) == finish:
                print(moveCount)
                found = True
                break
            if (not (nx,ny) in nub) and (not (nx,ny) in ndb) and (not (nx,ny) in nlb) and (not (nx,ny) in nrb):
                newPos.add((nx,ny))
        if found:
             break
    if found:
        break
    positions = newPos
    ub,db,lb,rb = nub,ndb,nlb,nrb