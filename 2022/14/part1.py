file1 = open('input.txt', 'r')
lines = file1.readlines()

cave = []
for line in [line.strip().split(' -> ') for line in lines]:
    for st,fi in zip(line[:-1],line[1:]):
        [stx,sty] = [int(x) for x in st.split(',')]
        [fix,fiy] = [int(x) for x in fi.split(',')]
        for x in range(min(stx,fix), max(stx,fix)+1):
            for y in range(min(sty,fiy), max(sty,fiy)+1):
                cave.append((x,y))
cave = list(set(cave))
maxDepth = max(cave, key = lambda t: t[1])[1]

placed = 0
fallForever = False
while True:
    if fallForever:
        break
    (x,y) = (500,0)
    while True:
        if y > maxDepth:
            fallForever = True
            break
        if not (x,y+1) in cave:
            y += 1
        elif not (x-1,y+1) in cave:
            x -= 1
            y += 1
        elif not (x+1,y+1) in cave:
            x += 1
            y += 1
        else:
            cave.append((x,y))
            placed += 1
            break
print(placed)