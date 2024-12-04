file1 = open('input.txt', 'r')
lines = file1.readlines()

mat = []
for line in lines:
    row = [x for x in line.strip()]
    mat.append(row)

rows = len(mat)
cols = len(mat[0])

res = 0
for x in range(rows):
    for y in range(cols):
        if mat[x][y] == 'X':
            if y >= 3 and ''.join(mat[x][y-3:y+1]) == 'SAMX':
                res += 1
            if y <= cols - 4 and ''.join(mat[x][y:y+4]) == 'XMAS':
                res += 1
            if x >= 3 and ''.join([row[y] for row in mat[x-3:x+1]]) =='SAMX':
                res += 1
            if x <= rows - 4 and ''.join([row[y] for row in mat[x:x+4]]) =='XMAS':
                res += 1
            if x >= 3 and y >= 3 and mat[x-1][y-1] + mat[x-2][y-2] + mat[x-3][y-3] == 'MAS':
                res += 1
            if x >= 3 and y <= cols - 4 and mat[x-1][y+1] + mat[x-2][y+2] + mat[x-3][y+3] == 'MAS':
                res += 1
            if x <= rows - 4 and y <= cols - 4 and mat[x+1][y+1] + mat[x+2][y+2] + mat[x+3][y+3] == 'MAS':
                res += 1
            if x <= rows - 4 and y >= 3 and mat[x+1][y-1] + mat[x+2][y-2] + mat[x+3][y-3] == 'MAS':
                res += 1

print(res)                