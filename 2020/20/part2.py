import numpy as np
import math
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))
file1 = open('input.txt', 'r')
lines = file1.readlines()

def isNeighbour(mat1, mat2):
    arr1 = [np.ravel(mat1[0,:]), 
            np.ravel(mat1[:,-1]),
            np.ravel(mat1[-1,:]), 
            np.ravel(mat1[:,0])
            ] # U,R,D,L
    
    arr2 = [np.ravel(mat2[0,:]), np.ravel(mat2[0,::-1]),
            np.ravel(mat2[:,-1]), np.ravel(mat2[::-1,-1]),
            np.ravel(mat2[-1,:]), np.ravel(mat2[-1,::-1]),
            np.ravel(mat2[:,0]), np.ravel(mat2[::-1,0])
            ] # U,R,D,L
    
    for i,a1 in enumerate(arr1):
        for j,a2 in enumerate(arr2):
            if np.array_equal(a1, a2):
                return i,j
    return -1,-1

mats = dict()

for i,line in enumerate(lines):
    if i % 12 == 0:
        currIndex = int(line.strip().split(' ')[1].split(':')[0])
    elif i % 12 == 1:
        arr = [list(line.strip())]
    elif 1 < (i % 12) < 10:
        arr.append(list(line.strip()))
    elif i % 12 == 10:
        arr.append(list(line.strip()))
        mats[currIndex] = np.matrix(arr)

notFound = [i for i in mats]
toFindNeighbours = []
placedMats = dict()
for num,i in enumerate(mats):
    if num == 0:
        placedMats[i] = (0,0)
        toFindNeighbours.append(i)
        notFound.remove(i)
     
while len(notFound) > 0:
    for i in toFindNeighbours:       
        for j in mats:
            if i == j or not(j in notFound):
                continue
            x,y = isNeighbour(mats[i],mats[j])
            if (x,y) != (-1,-1):
                target = (x+2)%4
                y = y//2
                if y >= target:
                    toRotate = y-target
                else:
                    toRotate = y+4-target
                mats[j] = np.rot90(mats[j], toRotate)
                (a,b) = placedMats[i]
                notFound.remove(j)
                toFindNeighbours.append(j)
                if x == 0:
                    placedMats[j] = a-1,b
                    if not np.array_equal(np.ravel(mats[i][0,:]),np.ravel(mats[j][-1,:])):
                        mats[j] = np.fliplr(mats[j])
                elif x == 1:
                    placedMats[j] = a,b+1
                    if not np.array_equal(np.ravel(mats[i][:,-1]),np.ravel(mats[j][:,0])):
                        mats[j] = np.flipud(mats[j])
                elif x == 2:
                    placedMats[j] = a+1,b
                    if not np.array_equal(np.ravel(mats[i][-1,:]),np.ravel(mats[j][0,:])):
                        mats[j] = np.fliplr(mats[j])
                elif x == 3:
                    placedMats[j] = a,b-1
                    if not np.array_equal(np.ravel(mats[i][:,0]),np.ravel(mats[j][:,-1])):
                        mats[j] = np.flipud(mats[j])
        toFindNeighbours.remove(i)
        
for i in mats:
    mats[i] = mats[i][1:-1,:]
    mats[i] = mats[i][:,1:-1]

dim = int(math.sqrt(len(mats)))
rows = []
count = 0
for i in dict(sorted(placedMats.items(), key=lambda item: item[1])):
    if count % dim == 0:
        if count != 0:
            rows.append(currRow)
        currRow = mats[i]
    else:
        currRow = np.hstack([currRow,mats[i]])
        if count == len(mats)-1:
            rows.append(currRow)
    count += 1
    
for i,row in enumerate(rows):
    if i == 0:
        fullMat = row
    else:
        fullMat = np.vstack([fullMat,row])
        
monster = [(0,0),(0,5),(0,6),(0,11),(0,12),(0,17),(0,18),(0,19),(1,1),(1,4),(1,7),(1,10),(1,13),(1,16),(-1,18)]

def findMonster(mat):
    global monster
    foundPos = []
    for i in range(1,len(mat)):
        for j in range(len(mat)-18):
            found = True
            for (a,b) in monster:
                if mat[i+a,j+b] != '#':
                    found = False
                    break
            if found:
                foundPos.append((i,j))
    return foundPos

while True:
    foundPos1 = findMonster(fullMat)
    foundPos2 = findMonster(np.fliplr(fullMat))
    foundPos3 = findMonster(np.flipud(fullMat))
    foundPos4= findMonster(np.fliplr(np.flipud(fullMat)))
    if len(foundPos1) + len(foundPos2) + len(foundPos3) == 0:
        fullMat = np.rot90(fullMat)
    else:
        break

if len(foundPos1) > 0:
    foundList = foundPos1
elif len(foundPos2) > 0:
    foundList = foundPos2
    fullMat = np.fliplr(fullMat)
elif len(foundPos3) > 0:
    foundList = foundPos3
    fullMat = np.flipud(fullMat)
else:
    foundList = foundPos4
    fullMat = np.fliplr(np.flipud(fullMat))
    
monsterPos = []
for (i,j) in foundList:
    for (a,b) in monster:
        monsterPos.append((i+a,j+b))
monsterPos = set(monsterPos)
print(np.count_nonzero(fullMat=='#')-len(monsterPos))
        