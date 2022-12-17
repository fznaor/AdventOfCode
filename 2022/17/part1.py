file1 = open('input.txt', 'r')
lines = file1.readlines()

commands = [x for x in lines[0].strip()]
commandIndex = 0
placed = set()
maxHeight = -1

for ii in range(2022):
    if ii % 5 == 0:
        newBlock = [(maxHeight+4,2),(maxHeight+4,3),(maxHeight+4,4),(maxHeight+4,5)]
    elif ii % 5 == 1:
        newBlock = [(maxHeight+4,3),(maxHeight+5,2),(maxHeight+5,3),(maxHeight+5,4),(maxHeight+6,3)]
    elif ii % 5 == 2:
        newBlock = [(maxHeight+4,2),(maxHeight+4,3),(maxHeight+4,4),(maxHeight+5,4),(maxHeight+6,4)]
    elif ii % 5 == 3:
        newBlock = [(maxHeight+4,2),(maxHeight+5,2),(maxHeight+6,2),(maxHeight+7,2)]
    else:
        newBlock = [(maxHeight+4,2),(maxHeight+4,3),(maxHeight+5,2),(maxHeight+5,3)]
    
    while True:
        canMove = True
        for i,j in newBlock:
            if commands[commandIndex] == '<':
                if j == 0 or (i,j-1) in placed:
                    canMove = False
                    break
            else:
                if j == 6 or (i,j+1) in placed:
                    canMove = False
                    break
        if canMove:
            newPos = []
            if commands[commandIndex] == '<':
                for i,j in newBlock:
                    newPos.append((i,j-1))
            else:
                for i,j in newBlock:
                    newPos.append((i,j+1))
            newBlock = newPos
        commandIndex += 1
        if commandIndex == len(commands):
            commandIndex = 0
        stopped = False
        for i,j in newBlock:
            if (i-1,j) in placed or i-1 < 0:
                placed.update(newBlock)
                for j,k in newBlock:
                    if j > maxHeight:
                        maxHeight = j
                stopped = True
                break
        if stopped:
            break
        newPos2 = []
        for i,j in newBlock:
            newPos2.append((i-1,j))
        newBlock = newPos2
print(maxHeight+1)