file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []
for line in lines:
    row = [x for x in line.strip()]
    mat.append(row)

rows = len(mat)
cols = len(mat[0])

res = 0
for x in range(1,rows-1):
    for y in range(1,cols-1):
        if mat[x][y] == 'A':
            if mat[x-1][y-1] + mat[x+1][y+1] in ('SM','MS') and mat[x-1][y+1] + mat[x+1][y-1] in ('SM','MS'):
                res += 1

print(res)                