file1 = open('input.txt', 'r')
lines = file1.readlines()

def isAdjacentToSymbol(arr, row, startCol, endCol):
    for i in range(row-1, row+2):
        for j in range(startCol-1, endCol+2):
            if i < 0 or i >= dim or j < 0 or j >= dim:
                continue
            if not arr[i][j].isdigit() and arr[i][j] != '.':
                return True
    return False

arr = []
dim = len(lines)
s = 0
for i,line in enumerate([line.strip() for line in lines]):
    j = 0
    while j < dim:
        numEnd = j
        if line[j].isdigit():
            while True:
                numEnd += 1
                if numEnd >= dim or not line[numEnd].isdigit():
                    break
            numEnd -= 1
        if line[j].isdigit():
            if isAdjacentToSymbol(lines, i, j, numEnd):
                s += int(line[j:numEnd+1])
            j = numEnd + 1
        else:
            j += 1
print(s)