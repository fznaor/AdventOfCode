file1 = open('input.txt', 'r')
lines = file1.readlines()

[minx,miny,maxx,maxy] = [0,0,4000000,4000000]
res = []
sensors = []
beacons = []
for line in [line.strip().split(' ') for line in lines]:
    [sx,sy] = [int(line[2].split('=')[1][:-1]), int(line[3].split('=')[1][:-1])]
    [bx,by] = [int(line[8].split('=')[1][:-1]), int(line[9].split('=')[1])]
    sensors.append((sx,sy))
    beacons.append((bx,by))
    
for y in range(maxy+1):
    ranges = []
    for (sx,sy),(bx,by) in zip(sensors,beacons):
        dist = abs(sx-bx) + abs(sy-by)
        distToTarget = abs(y-sy)
        d = dist-distToTarget
        if d >= 0:
            if sx-d <= maxx and sx+d>=minx:
                lo = minx if sx-d < minx else sx-d
                hi = maxx if sx+d > maxx else sx+d
                ranges.append([lo, hi])
    union = []
    for begin,end in sorted(ranges):
        if union and union[-1][1] >= begin - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([begin, end])
    if len(union) > 1:
        print((union[0][1]+1)*4000000+y)
        break
