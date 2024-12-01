import hashlib

inp = 'pxxbnzuo'
initLength = len(inp)
shortestPath = ''

def move(inp, pos):
    global shortestPath
    if len(inp[initLength:]) > len(shortestPath) and shortestPath != '':
        return
    [x,y] = pos
    if x == 3 and y == 3:
        if shortestPath == '':
            shortestPath = inp[initLength:]
        elif len(inp[initLength:]) < len(shortestPath):
            shortestPath = inp[initLength:]
        return
    hash = hashlib.md5((inp).encode('utf-8')).hexdigest()
    if hash[0] in ['b','c','d','e','f'] and x > 0:
        move(inp + 'U', [x-1,y])
    if hash[1] in ['b','c','d','e','f'] and x < 3:
        move(inp + 'D', [x+1,y])
    if hash[2] in ['b','c','d','e','f'] and y > 0:
        move(inp + 'L', [x,y-1])
    if hash[3] in ['b','c','d','e','f'] and y < 3:
        move(inp + 'R', [x,y+1])

move(inp, [0,0])
print(shortestPath)