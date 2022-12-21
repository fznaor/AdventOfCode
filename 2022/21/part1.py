file1 = open('input.txt', 'r')
lines = file1.readlines()

monkeys = {}
lines = [line.strip().split(' ') for line in lines]
doneLines = []

found = False
while True:
    for i,line in enumerate(lines):
        if not i in doneLines:
            if len(line) == 2:
                monkeys[line[0][:-1]] = int(line[1])
                doneLines.append(i)
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
                    if 'root' in monkeys:
                        print(monkeys['root'])
                        found = True
                        break
    if found:
        break