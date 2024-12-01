from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

file1 = open('input.txt', 'r')
lines = file1.readlines()

maze = []
startPos = []
for i,line in enumerate([line.strip() for line in lines]):
    maze.append([x for x in line])
    sPos = line.find('S')
    if sPos != -1:
        startPos = [i, sPos]
points = []
points.append(startPos)

dist = [[-1 for i in range(len(maze))] for j in range(len(maze))]
dist[startPos[0]][startPos[1]] = 0

def move(direction, x, y):
    global startPos, maze

    points.append([x,y])

    newDir = '.'

    if direction == 'N' and x-1 >= 0:
        newPos = maze[x-1][y]
        if newPos == '|':
            newDir = 'N'
        elif newPos == 'F':
            newDir = 'E'
        elif newPos == '7':
            newDir = 'W'
        if newDir != '.' or newPos == 'S':
            return newDir, x-1, y
    elif direction == 'S' and x+1 < len(maze):
        newPos = maze[x+1][y]
        if newPos == '|':
            newDir = 'S'
        elif newPos == 'L':
            newDir = 'E'
        elif newPos == 'J':
            newDir = 'W'
        if newDir != '.' or newPos == 'S':
            return newDir, x+1, y
    if direction == 'W' and y-1 >= 0:
        newPos = maze[x][y-1]
        if newPos == '-':
            newDir = 'W'
        elif newPos == 'L':
            newDir = 'N'
        elif newPos == 'F':
            newDir = 'S'
        if newDir != '.' or newPos == 'S':
            return newDir, x, y-1
    if direction == 'E' and y+1 < len(maze):
        newPos = maze[x][y+1]
        if newPos == '-':
            newDir = 'E'
        elif newPos == 'J':
            newDir = 'N'
        elif newPos == '7':
            newDir = 'S'
        if newDir != '.' or newPos == 'S':
            return newDir, x, y+1

sX, sY = startPos
newDir = ''
if sX-1 >= 0:
    if maze[sX-1][sY] == '|':
        sX -= 1
        newDir = 'N'
    elif maze[sX-1][sY] == '7':
        sX -= 1
        newDir = 'W'
    elif maze[sX-1][sY] == 'F':
        sX -= 1
        newDir = 'E'
if newDir == '' and sX+1 < len(maze):
    if maze[sX+1][sY] == '|':
        sX += 1
        newDir = 'S'
    if maze[sX+1][sY] == 'L':
        sX += 1
        newDir = 'E'
    if maze[sX+1][sY] == 'J':
        sX += 1
        newDir = 'W'
if newDir == '' and sY-1 >= 0:
    if maze[sX][sY-1] == '-':
        sY -= 1
        newDir = 'W'
    if maze[sX][sY-1] == 'L':
        sY -= 1
        newDir = 'N'
    if maze[sX][sY-1] == 'F':
        sY -= 1
        newDir = 'S'

while [sX, sY] != startPos:
    newDir, sX, sY = move(newDir, sX, sY)

s = 0
polygon = Polygon(points)
for i in range(len(maze)):
    for j in range(len(maze)):
        if polygon.contains(Point(i,j)):
            s += 1
print(s)