file1 = open('input.txt', 'r')
lines = file1.readlines()

monkeys = {}
lines = [line.strip().split(' ') for line in lines]
doneLines = []

while True:
    foundNew = False
    for i,line in enumerate(lines):
        if not i in doneLines:
            if len(line) == 2 and line[0][:-1] != 'humn':
                monkeys[line[0][:-1]] = int(line[1])
                doneLines.append(i)
                foundNew = True
            else:
                if line[1] in monkeys and line[3] in monkeys:
                    doneLines.append(i)
                    if line[2] == '+':
                        monkeys[line[0][:-1]] = monkeys[line[1]] + monkeys[line[3]]
                    elif line[2] == '-':
                        monkeys[line[0][:-1]] = monkeys[line[1]] - monkeys[line[3]]
                    elif line[2] == '*':
                        monkeys[line[0][:-1]] = monkeys[line[1]] * monkeys[line[3]]
                    elif line[2] == '/':
                        monkeys[line[0][:-1]] = monkeys[line[1]] // monkeys[line[3]]
                    foundNew = True
            if line[0][:-1] == 'humn':
                hind = i
    if not foundNew:
        break
    
doneLines.append(hind)
lo = 1000000000000
hi = 10000000000000
h = hi
delta = (hi-lo)//4
foundRes = False
prev = "None"
while True:
    tmonkeys = monkeys.copy()
    tdoneLines = doneLines.copy()
    tmonkeys['humn'] = h
    found = False
    while True:
        for i,line in enumerate(lines):
            if not i in tdoneLines:
                if len(line) > 2:
                    if line[1] in tmonkeys and line[3] in tmonkeys:
                        tdoneLines.append(i)
                        if line[0][:-1] == 'root':
                            print(h,tmonkeys[line[1]],tmonkeys[line[3]])
                            if tmonkeys[line[1]] == tmonkeys[line[3]]:
                                foundRes = True
                            else:
                                if tmonkeys[line[1]] > tmonkeys[line[3]]:
                                    higher = True
                                else:
                                    higher = False
                            found = True
                            break
                        if line[2] == '+':
                            tmonkeys[line[0][:-1]] = tmonkeys[line[1]] + tmonkeys[line[3]]
                        elif line[2] == '-':
                            tmonkeys[line[0][:-1]] = tmonkeys[line[1]] - tmonkeys[line[3]]
                        elif line[2] == '*':
                            tmonkeys[line[0][:-1]] = tmonkeys[line[1]] * tmonkeys[line[3]]
                        elif line[2] == '/':
                            tmonkeys[line[0][:-1]] = tmonkeys[line[1]] // tmonkeys[line[3]]
        if found:
            break
    if foundRes:
        print(h)
        break
    print(higher)
    if higher:
        if prev == "lower":
            delta //= 2
        h += delta
        prev = "higher"
    else:
        if prev == "higher":
            delta //= 2
        h -= delta
        prev = "lower"