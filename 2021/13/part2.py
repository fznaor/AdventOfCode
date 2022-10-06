import numpy as np
l_w = 1000 #The number of elements to display before truncation in console
np.set_printoptions(linewidth=l_w)

file1 = open('input.txt', 'r')
lines = file1.readlines()

points = []
folds = []
readPoints = True
for line in lines:
    if len(line) == 1:
        readPoints = False
        continue
    if readPoints:
        points.append((int(line.rstrip().split(',')[0]),int(line.rstrip().split(',')[1])))
    else:
        split = line.rstrip().split('along ')[1]
        folds.append((split.split('=')[0], int(split.split('=')[1])))
        
for fold in folds:
    if fold[0] == 'y':
        for i in range(len(points)):
            if points[i][1] < fold[1]:
                continue
            else:
                newPoint = list(points[i])
                newPoint[1] = 2*fold[1] - newPoint[1]
                newPoint = tuple(newPoint)
                points[i] = newPoint
    elif fold[0] == 'x':
        for i in range(len(points)):
            if points[i][0] < fold[1]:
                continue
            else:
                newPoint = list(points[i])
                newPoint[0] = 2*fold[1] - newPoint[0]
                newPoint = tuple(newPoint)
                points[i] = newPoint
    points = list(set(points))
    
maxX = 0
maxY = 0

for point in points:
    if point[0] > maxX:
        maxX = point[0]
    if point[1] > maxY:
        maxY = point[1]
        
pointArr = np.full((maxY+1, maxX+1), '.')

for y in range(maxY+1):
    for x in range(maxX+1):
        if (x,y) in points:
            pointArr[y][x] = '#'

print(pointArr)