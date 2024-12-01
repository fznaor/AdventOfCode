file1 = open('input.txt', 'r')
lines = file1.readlines()

prevRow = [x for x in lines[0].strip()]
safeCount = prevRow.count('.')

i = 1
while i <= 399999:
    newRow = []
    for j in range(len(prevRow)):
        left = prevRow[j-1] if j-1 >= 0 else '.'
        center = prevRow[j]
        right = prevRow[j+1] if j+1 < len(prevRow) else '.'

        if (left,center,right) in [('^','^','.'),('.','^','^'),('^','.','.'),('.','.','^')]:
            newRow.append('^')
        else:
            newRow.append('.')
    prevRow = newRow
    safeCount += prevRow.count('.')
    i += 1
print(safeCount)