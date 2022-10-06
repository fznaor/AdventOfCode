import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()
active = np.zeros([101, 101, 101])

for line in lines:
    [command, coords] = line.rstrip().split(' ')
    [xCoords, yCoords, zCoords] = coords.split(',')
    [xLower, xUpper] = [int(a) for a in xCoords.split('=')[1].split('..')]
    [yLower, yUpper] = [int(a) for a in yCoords.split('=')[1].split('..')]
    [zLower, zUpper] = [int(a) for a in zCoords.split('=')[1].split('..')]
    for i in range(max(-50, xLower), min(51, xUpper + 1)):
        for j in range(max(-50, yLower), min(51, yUpper + 1)):
            for k in range(max(-50, zLower), min(51, zUpper + 1)):
                current = active[i+50][j+50][k+50]
                if command == 'on':
                    if current == 0:
                        active[i + 50][j + 50][k + 50] = 1
                else:
                    if current == 1:
                        active[i + 50][j + 50][k + 50] = 0
print(np.sum(active == 1))
