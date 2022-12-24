file1 = open('input.txt', 'r')
lines = file1.readlines()
import re

mat = dict()
d = 0 # eswn

parsingMat = True
for i,line in enumerate([line for line in lines]):
    if len(line.strip()) == 0:
        parsingMat = False
        continue
    
    if parsingMat:
        for j,z in enumerate(line[:-1]):
            if z != ' ':
                mat[(i+1,j+1)] = z
                if len(mat) == 1:
                    (x,y) = (i+1,j+1)
    else:
        strlist = re.split('(\d+)', line.strip())[1:-1]
        for s in strlist:    
            if s.isnumeric():
                num = int(s)
                if d == 0:
                    for j in range(num):
                        if (x,y+1) in mat:
                            if mat[(x,y+1)] == '#':
                                   break
                            else:
                                y = y+1
                        else:
                            k = 1
                            while True:
                                if (x,k) in mat:
                                    break
                                k += 1
                            if mat[(x,k)] == '#':
                                break
                            else:
                                y = k
                elif d == 2:
                    for j in range(num):
                        if (x,y-1) in mat:
                            if mat[(x,y-1)] == '#':
                                   break
                            else:
                                y = y-1
                        else:
                            k = len(lines[0])+1
                            while True:
                                if (x,k) in mat:
                                    break
                                k -= 1
                            if mat[(x,k)] == '#':
                                break
                            else:
                                y = k
                elif d == 1:
                    for j in range(num):
                        if (x+1,y) in mat:
                            if mat[(x+1,y)] == '#':
                                   break
                            else:
                                x = x+1
                        else:
                            k = 1
                            while True:
                                if (k,y) in mat:
                                    break
                                k += 1
                            if mat[(k,y)] == '#':
                                break
                            else:
                                x = k
                elif d == 3:
                    for j in range(num):
                        if (x-1,y) in mat:
                            if mat[(x-1,y)] == '#':
                                   break
                            else:
                                x = x-1
                        else:
                            k = len(lines)+1
                            while True:
                                if (k,y) in mat:
                                    break
                                k -= 1
                            if mat[(k,y)] == '#':
                                break
                            else:
                                x = k
            else:
                if s == 'L':
                    d -= 1
                else:
                    d += 1
                d %= 4
print(1000*x + 4*y + d)
            