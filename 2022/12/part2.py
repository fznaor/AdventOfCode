import numpy as np
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []

for line in lines:
    arr.append([a for a in line.rstrip()])
    
arr = np.array(arr)
height = arr.shape[0]
width = arr.shape[1]

[endx,endy] = [np.where(arr=='E')[0][0], np.where(arr=='E')[1][0]]
arr[endx][endy] = 'z'
[startx,starty] = [np.where(arr=='S')[0][0], np.where(arr=='S')[1][0]]
arr[startx][starty] = 'a'

startLocations = []

for i,j in zip(np.where(arr=='a')[0], np.where(arr=='a')[1]):
    startLocations.append((i,j))
    

dist = np.full((height, width), math.inf)

dist[endx][endy] = 0

visited = np.full((height, width), False)


while True:
    minV = math.inf
    minX = endx
    minY = endy
    for ii in range(height):
        for jj in range(width):
            if visited[ii][jj]:
                continue
            if dist[ii][jj] < minV:
                minV = dist[ii][jj]
                minX = ii
                minY = jj
    if minX == i and minY == j:
        break
    i = minX
    j = minY
    
    if arr[i][j] == 'a':
        break
    
    if j<width-1:
        if ord(arr[i][j+1]) >= ord(arr[i][j])-1:
            alt = dist[i][j] + 1
            if alt < dist[i][j+1]:
                dist[i][j+1] = alt
    if j>0:
        if ord(arr[i][j-1]) >= ord(arr[i][j])-1:
            alt = dist[i][j] + 1
            if alt < dist[i][j-1]:
                dist[i][j-1] = alt
    if i<height-1:
        if ord(arr[i+1][j]) >= ord(arr[i][j])-1:
            alt = dist[i][j] + 1
            if alt < dist[i+1][j]:
                dist[i+1][j] = alt
    if i>0:
        if ord(arr[i-1][j]) >= ord(arr[i][j])-1:
            alt = dist[i][j] + 1
            if alt < dist[i-1][j]:
                dist[i-1][j] = alt
    visited[i][j] = True

print(int(dist[i][j]))