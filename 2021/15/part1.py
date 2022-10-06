import numpy as np
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []

for line in lines:
    arr.append([int(a) for a in line.rstrip()])
    
arr = np.array(arr)
height = arr.shape[0]
width = arr.shape[1]

dist = np.full((width, height), math.inf)
dist[0][0] = 0
visited = np.full((width, height), False)

while True:
    minV = math.inf
    minX = 0
    minY = 0
    for i in range(width):
        for j in range(height):
            if visited[i][j]:
                continue
            if dist[i][j] < minV:
                minV = dist[i][j]
                minX = i
                minY =j
    i = minX
    j = minY
    
    if i == height-1 and j==width-1:
        break
    
    if j<width-1:
        alt = dist[i][j] + arr[i][j+1]
        if alt < dist[i][j+1]:
            dist[i][j+1] = alt
    if j>0:
        alt = dist[i][j] + arr[i][j-1]
        if alt < dist[i][j-1]:
            dist[i][j-1] = alt
    if i<height-1:
        alt = dist[i][j] + arr[i+1][j]
        if alt < dist[i+1][j]:
            dist[i+1][j] = alt
    if i>0:
        alt = dist[i][j] + arr[i-1][j]
        if alt < dist[i-1][j]:
            dist[i-1][j] = alt
    visited[i][j] = True

print(dist[height-1][width-1])