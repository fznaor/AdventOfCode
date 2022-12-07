file1 = open('input.txt', 'r')
lines = file1.readlines()

onLights = dict()
for line in lines:
    line = line.strip().split(' ')
    if line[0] == 'turn':
        op = line[1]
        [x1,y1] = [int(x) for x in line[2].split(',')]
        [x2,y2] = [int(x) for x in line[4].split(',')]
    else:
        op = line[0]
        [x1,y1] = [int(x) for x in line[1].split(',')]
        [x2,y2] = [int(x) for x in line[3].split(',')]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if op == 'on':
                if (x,y) not in onLights:
                    onLights[(x,y)] = 1
                else:
                    onLights[(x,y)] += 1
            elif op == 'off':
                if (x,y) in onLights:
                    onLights[(x,y)] -= 1
                    if onLights[(x,y)] == 0:
                        onLights.pop((x,y), None)
            else:
                if (x,y) not in onLights:
                    onLights[(x,y)] = 2
                else:
                    onLights[(x,y)] += 2
res = 0
for (x,y) in onLights:
    res += onLights[(x,y)]
print(res)