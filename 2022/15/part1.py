file1 = open('input.txt', 'r')
lines = file1.readlines()

targetY = 2000000
res = []
for line in [line.strip().split(' ') for line in lines]:
    [sx,sy] = [int(line[2].split('=')[1][:-1]), int(line[3].split('=')[1][:-1])]
    [bx,by] = [int(line[8].split('=')[1][:-1]), int(line[9].split('=')[1])]
    dist = abs(sx-bx) + abs(sy-by)
    distToTarget = abs(targetY-sy)
    for i in range(dist-distToTarget+1):
        if not (by == targetY and sx-i == bx):
            res.append(sx-i)
        if not (by == targetY and sx+i == bx):
            res.append(sx+i)
res = list(set(res))
print(len(res))