file1 = open('input.txt', 'r')
lines = file1.readlines()

xRange = lines[0].rstrip().split('x=')[1].split(',')[0]
yRange = lines[0].rstrip().split('y=')[1]

[xLow, xHi] = [int(i) for i in xRange.split('..')]
[yLow, yHi] = [int(i) for i in yRange.split('..')]

suma = 0
minX = 0
maxX = xHi
minY = yLow
maxY = abs(yLow) - 1
while True:
    minX += 1
    suma += minX
    if suma >= xLow:
        break
    
xSteps = {}
res = 0
    
for x in range(minX, maxX + 1):
    for y in range(minY, maxY + 1):
        xMove = x
        yMove = y
        xx = 0
        yy = 0
        while True:
            xx += xMove
            yy += yMove
            if xMove != 0:
                xMove -= 1
            yMove -= 1
            if xx in range(xLow, xHi+1) and yy in range(yLow, yHi+1):
                res += 1
                break
            if xx > xHi:
                break
            if yy < yLow:
                break
print(res)