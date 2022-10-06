file1 = open('input.txt', 'r')
lines = file1.readlines()

blackTiles = []

def countBlackNeighbours(i,j):
    count = 0
    if (i-2, j) in blackTiles:
        count += 1
    if (i+2, j) in blackTiles:
        count += 1
    if (i-1, j-1) in blackTiles:
        count += 1
    if (i-1, j+1) in blackTiles:
        count += 1
    if (i+1, j-1) in blackTiles:
        count += 1
    if (i+1, j+1) in blackTiles:
        count += 1
    return count

for line in lines:
    line = line.rstrip()
    
    command = ''
    i = 0
    j = 0
    for letter in line:
        if letter in ['s', 'n']:
            command += letter
        else:
            command += letter
            if command == 'w':
                i -= 2
            elif command == 'e':
                i += 2
            elif command == 'se':
                j -= 1
                i += 1
            elif command == 'sw':
                j -= 1
                i -= 1
            elif command == 'ne':
                j += 1
                i += 1
            elif command == 'nw':
                j += 1
                i -= 1
            command = ''
    if (i,j) not in blackTiles:
        blackTiles.append((i,j))
    else:
        blackTiles.remove((i,j))

for it in range(100):
    visited = []
    newList = []
    for (i,j) in blackTiles:
        if countBlackNeighbours(i,j) in [1,2]:
            newList.append((i,j))
        for (ii,jj) in [(i-2,j), (i+2,j), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]:
            if (ii,jj) not in visited and (ii,jj) not in blackTiles:
                visited.append((ii,jj))
                if countBlackNeighbours(ii,jj) == 2:
                    newList.append((ii,jj))
    blackTiles = newList
print(len(blackTiles))