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

dist = np.full((height, width), math.inf)
[startx,starty] = [np.where(arr=='S')[0][0], np.where(arr=='S')[1][0]]
dist[startx][starty] = 0
arr[startx][starty] = 'a'
visited = np.full((height, width), False)

[endx,endy] = [np.where(arr=='E')[0][0], np.where(arr=='E')[1][0]]
arr[endx][endy] = 'z'

while True:
    minV = math.inf
    minX = startx
    minY = starty
    for i in range(height):
        for j in range(width):
            if visited[i][j]:
                continue
            if dist[i][j] < minV:
                minV = dist[i][j]
                minX = i
                minY =j
    i = minX
    j = minY
    
    if (i,j) == (endx,endy):
        break
    
    if j<width-1:
        if ord(arr[i][j+1]) <= ord(arr[i][j])+1:
            alt = dist[i][j] + 1
            if alt < dist[i][j+1]:
                dist[i][j+1] = alt
    if j>0:
        if ord(arr[i][j-1]) <= ord(arr[i][j])+1:
            alt = dist[i][j] + 1
            if alt < dist[i][j-1]:
                dist[i][j-1] = alt
    if i<height-1:
        if ord(arr[i+1][j]) <= ord(arr[i][j])+1:
            alt = dist[i][j] + 1
            if alt < dist[i+1][j]:
                dist[i+1][j] = alt
    if i>0:
        if ord(arr[i-1][j]) <= ord(arr[i][j])+1:
            alt = dist[i][j] + 1
            if alt < dist[i-1][j]:
                dist[i-1][j] = alt
    visited[i][j] = True

print(int(dist[i][j]))