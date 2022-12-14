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
floor = maxDepth + 2

count = 1
depth = 0
row = [(500,0)]
while depth < floor - 1:
    newRow = []
    for (i,j) in row:
        if not (i-1,j+1) in cave:
            newRow.append((i-1,j+1))
        if not (i,j+1) in cave:
            newRow.append((i,j+1))
        if not (i+1,j+1) in cave:
            newRow.append((i+1,j+1))
    newRow = list(set(newRow))
    count += len(newRow)
    row = newRow
    depth += 1
print(count)