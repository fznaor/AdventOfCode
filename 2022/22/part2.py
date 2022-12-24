file1 = open('input.txt', 'r')
lines = file1.readlines()
import re

mats = dict()
d = 0 # eswn

nbrs = dict()
nbrs[1] = {'u': 9, 'd': 4, 'l': 6, 'r': 2}
nbrs[2] = {'u': 9, 'd': 4, 'l': 1, 'r': 7}
nbrs[4] = {'u': 1, 'd': 7, 'l': 6, 'r': 2}
nbrs[6] = {'u': 4, 'd': 9, 'l': 1, 'r': 7}
nbrs[7] = {'u': 4, 'd': 9, 'l': 6, 'r': 2}
nbrs[9] = {'u': 6, 'd': 2, 'l': 1, 'r': 7}

parsingMat = True
DIM = len(lines[0][:-1]) // 3
for i,line in enumerate([line for line in lines]):
    if len(line.strip()) == 0:
        parsingMat = False
        continue
    
    if parsingMat:
        l = line[:-1]
        for j,z in enumerate(l):
            if z != ' ':
                sqIndex = 3 * (i //((len(lines)-2)//4)) + j //(len(lines[0][:-1])//3)
                if not sqIndex in mats:
                    mats[sqIndex] = dict()
                mats[sqIndex][((i % ((len(lines)-2)//4)), j % (len(lines[0][:-1])//3))] = z
    else:
        strlist = re.split('(\d+)', line.strip())[1:-1]
        currMat = 1
        x,y = 0,0
        for s in strlist:
            if s.isnumeric():
                num = int(s)
                for ii in range(num):
                    changeMat = False
                    if d == 2:
                        if y > 0:
                            if mats[currMat][(x,y-1)] == '#':
                                break
                            else:
                                y -= 1
                        else:
                            changeMat = True
                            dest = nbrs[currMat]['l']
                            orD = 'l'
                            for z in nbrs[dest]:
                                if nbrs[dest][z] == currMat:
                                    deD = z
                                    break
                    elif d == 0:
                        if y < DIM-1:
                            if mats[currMat][(x,y+1)] == '#':
                                break
                            else:
                                y += 1
                        else:
                            changeMat = True
                            dest = nbrs[currMat]['r']
                            orD = 'r'
                            for z in nbrs[dest]:
                                if nbrs[dest][z] == currMat:
                                    deD = z
                                    break
                    elif d == 1:
                        if x < DIM-1:
                            if mats[currMat][(x+1,y)] == '#':
                                break
                            else:
                                x += 1
                        else:
                            changeMat = True
                            dest = nbrs[currMat]['d']
                            orD = 'd'
                            for z in nbrs[dest]:
                                if nbrs[dest][z] == currMat:
                                    deD = z
                                    break
                    elif d == 3:
                        if x > 0:
                            if mats[currMat][(x-1,y)] == '#':
                                break
                            else:
                                x -= 1
                        else:
                            changeMat = True
                            dest = nbrs[currMat]['u']
                            orD = 'u'
                            for z in nbrs[dest]:
                                if nbrs[dest][z] == currMat:
                                    deD = z
                                    break
                    if changeMat:
                        if orD == 'd' and deD == 'u':
                            xx = 0
                            yy = y
                            dd = 1
                        elif orD == 'd' and deD == 'r':
                            xx = y
                            yy = DIM-1
                            dd = 2
                        elif orD == 'r' and deD == 'l':
                            xx = x
                            yy = 0
                            dd = 0
                        elif orD == 'r' and deD == 'r':
                            xx = DIM-x-1
                            yy = DIM-1
                            dd = 2
                        elif orD == 'r' and deD == 'd':
                            xx = DIM-1
                            yy = x
                            dd = 3
                        elif orD == 'l' and deD == 'u':
                            xx = 0
                            yy = x
                            dd = 1
                        elif orD == 'u' and deD == 'l':
                            xx = y
                            yy = 0
                            dd = 0
                        elif orD == 'l' and deD == 'l':
                            xx = DIM-x-1
                            yy = 0
                            dd = 0
                        elif orD == 'l' and deD == 'r':
                            xx = x
                            yy = DIM-1
                            dd = 2
                        elif orD == 'u' and deD == 'd':
                            xx = DIM-1
                            yy = y
                            dd = 3
                        if mats[dest][(xx,yy)] == '#':
                            break
                        else:
                            currMat = dest
                            x,y = xx,yy
                            d = dd
            else:
                if s == 'L':
                    d -= 1
                else:
                    d += 1
                d %= 4
xx = (currMat // 3) * DIM + x + 1
yy = (currMat % 3) * DIM + y + 1
print(1000*xx + 4*yy + d)