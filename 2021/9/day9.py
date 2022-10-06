file1 = open('v21.txt', 'r')
lines = file1.readlines()

val = []

for line in lines:
    val.append(list(line.rstrip()))

height = len(val)
width = len(val[0])

val = [list(map(int, i)) for i in val]

floodres = 0
results = []
status = [[0 for i in range(width)] for j in range(height)]


def floodfill(i, j):
    global status
    global floodres
    if val[i][j] == 9:
        return
    if status[i][j] == 1:
        return
    status[i][j] = 1
    floodres += 1
    if j != width - 1:
        if val[i][j + 1] > val[i][j]:
            floodfill(i, j + 1)
    if j != 0:
        if val[i][j - 1] > val[i][j]:
            floodfill(i, j - 1)
    if i != height - 1:
        if val[i + 1][j] > val[i][j]:
            floodfill(i + 1, j)
    if i != 0:
        if val[i - 1][j] > val[i][j]:
            floodfill(i - 1, j)


for i in range(height):
    for j in range(width):
        if i == 0 and j == 0:
            if val[i][j] < val[0][1] and val[i][j] < val[1][0]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
                status = [[0 for i in range(width)] for j in range(height)]
        elif i == 0 and j == width - 1:
            if val[i][j] < val[0][width - 2] and val[i][j] < val[1][width - 1]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        elif i == height - 1 and j == 0:
            if val[i][j] < val[height - 1][1] and val[i][j] < val[height - 2][0]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        elif i == height - 1 and j == width - 1:
            if val[i][j] < val[height - 2][width - 1] and val[i][j] < val[height - 1][width - 2]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
                status = [[0 for i in range(width)] for j in range(height)]
        elif i == 0:
            if val[i][j] < val[i][j + 1] and val[i][j] < val[i][j - 1] and val[i][j] < val[i + 1][j]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        elif i == height - 1:
            if val[i][j] < val[i][j + 1] and val[i][j] < val[i][j - 1] and val[i][j] < val[i - 1][j]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        elif j == 0:
            if val[i][j] < val[i][j + 1] and val[i][j] < val[i + 1][j] and val[i][j] < val[i - 1][j]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        elif j == width - 1:
            if val[i][j] < val[i][j - 1] and val[i][j] < val[i + 1][j] and val[i][j] < val[i - 1][j]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0
        else:
            if val[i][j] < val[i][j + 1] and val[i][j] < val[i][j - 1] and val[i][j] < val[i + 1][j] and val[i][j] < \
                    val[i - 1][j]:
                floodfill(i, j)
                results.append(floodres)
                floodres = 0

results.sort()
print(results[-1] * results[-2] * results[-3])
