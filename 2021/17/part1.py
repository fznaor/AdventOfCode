file1 = open('input.txt', 'r')
lines = file1.readlines()

xRange = lines[0].rstrip().split('x=')[1].split(',')[0]
yRange = lines[0].rstrip().split('y=')[1]

[xLow, xHi] = [int(i) for i in xRange.split('..')]
[yHi, yLow] = [int(i) for i in yRange.split('..')]

print(abs(yHi+1) * (abs(yHi+1) + 1) / 2)