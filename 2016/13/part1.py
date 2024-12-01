from collections import deque

favNum = 1358
goalX = 31
goalY = 39

visited = []

def isWall(x,y):
    global favNum
    
    num = x*x + 3*x + 2*x*y + y + y*y + favNum
    return bin(num).count("1") % 2 == 1

queue = deque([((1,1), 0)])
seen = set()

while queue:
    (x,y), distance = queue.popleft()
    if (x,y) in seen:
        continue
    seen.add((x,y))
    if (x,y) == (goalX, goalY):
        print(distance)
        break
    if x-1 >= 0 and not isWall(x-1,y) and (x-1,y) not in visited:
        queue.append([(x-1,y), distance+1])
    if not isWall(x+1,y) and (x+1,y) not in visited:
        queue.append([(x+1,y), distance+1])
    if y-1 >= 0 and not isWall(x,y-1) and (x,y-1) not in visited:
        queue.append([(x,y-1), distance+1])
    if not isWall(x,y+1) and (x,y+1) not in visited:
        queue.append([(x,y+1), distance+1])