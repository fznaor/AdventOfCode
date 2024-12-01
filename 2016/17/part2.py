import hashlib

inp = 'pxxbnzuo'
initLength = len(inp)
longestPathLength = 0

def move(inp, pos):
    global longestPathLength
    [x,y] = pos
    if x == 3 and y == 3:
        if len(inp[initLength:]) > longestPathLength:
            longestPathLength = len(inp[initLength:])
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
print(longestPathLength)