file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []
for line in [line.strip() for line in lines]:
    row = [int(a) for a in line]
    arr.append(row)
    
rows = len(arr)
cols = len(arr[0])
visible = []

for i in range(rows):
    high = -1
    for j in range(cols):
        if arr[i][j] > high:
            high = arr[i][j]
            visible.append((i,j))
    high = -1
    for j in range(cols-1,-1,-1):
        if arr[i][j] > high:
            high = arr[i][j]
            visible.append((i,j))
            
for j in range(cols):
    high = -1
    for i in range(rows):
        if arr[i][j] > high:
            high = arr[i][j]
            visible.append((i,j))
    high = -1
    for i in range(rows-1,-1,-1):
        if arr[i][j] > high:
            high = arr[i][j]
            visible.append((i,j))
print(len(set(visible)))