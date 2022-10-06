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
    print(len(points))
    break