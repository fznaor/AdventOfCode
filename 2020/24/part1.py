file1 = open('input.txt', 'r')
lines = file1.readlines()

blackTiles = []

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
print(len(blackTiles))