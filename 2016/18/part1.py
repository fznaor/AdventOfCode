file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = [[x for x in lines[0].strip()]]

i = 1
while i <= 39:
    newRow = []
    for j in range(len(arr[0])):
        left = arr[i-1][j-1] if j-1 >= 0 else '.'
        center = arr[i-1][j]
        right = arr[i-1][j+1] if j+1 < len(arr[0]) else '.'

        if (left,center,right) in [('^','^','.'),('.','^','^'),('^','.','.'),('.','.','^')]:
            newRow.append('^')
        else:
            newRow.append('.')
    arr.append(newRow)
    i += 1
print(sum(x.count('.') for x in arr))