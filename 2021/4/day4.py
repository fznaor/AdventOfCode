import numpy as np

file1 = open('v21.txt', 'r')
lines = file1.readlines()

inputs = lines[0].rstrip().split(',')

bingoBoards = []
newBoard = []

for i in range(2,len(lines)):
    if(len(lines[i])==1):
        bingoBoards.append(newBoard)
        newBoard = []
    else:
        lines[i] = " ".join(lines[i].split())
        row = lines[i].rstrip().strip().split(' ')
        newBoard.append(row)
bingoBoards.append(newBoard)

def isBingo(states):
    for i in range(5):
        for j in range(5):
            if states[i][j] == False:
                break
            if j==4:
                return True
    for j in range(5):
        for i in range(5):
            if states[i][j] == False:
                break
            if i==4:
                return True
    return False

def checkWhenBingo(board):
    states = []
    for i in range(5):
        states.append([False,False,False,False,False])
    drawnNumbers = 0
    for num in inputs:
        drawnNumbers += 1
        for i in range(5):
            for j in range(5):
                if(int(board[i][j])==int(num)):
                    states[i][j] = True
                    if isBingo(states):
                        suma = 0
                        for k in range(5):
                            for l in range(5):
                                if states[k][l] == False:
                                    suma += int(board[k][l])
                        return [drawnNumbers, suma*int(num)]
                
maxDrawn = 0
maxDrawnScore = 0
for board in bingoBoards:
    [drawn, score] = checkWhenBingo(board)
    if drawn > maxDrawn:
        maxDrawn = drawn
        maxDrawnScore = score
print(maxDrawnScore)