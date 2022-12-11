file1 = open('input.txt', 'r')
lines = file1.readlines()

currMonkey = -1
monkeys = []
ops = []
rhs = []
tests = []
true = []
false = []

for line in [line.strip() for line in lines]:
    if line.startswith('Monkey'):
        currMonkey = int(line.split(' ')[1][:-1])
    elif line.startswith('Starting'):
        items = [int(x) for x in line[16:].split(', ')]
        monkeys.append(items)
    elif line.startswith('Operation'):
        line = line.split(' ')
        ops.append(line[4])
        rhs.append(line[5])
    elif line.startswith('Test'):
        tests.append(int(line.split(' ')[3]))
    elif line.startswith('If true'):
        true.append(int(line.split(' ')[5]))
    elif line.startswith('If false'):
        false.append(int(line.split(' ')[5]))
        
monkeyMods = []
for monkey in monkeys:
    newMods = []
    for m in monkey:
        mods = []
        for t in tests:
            mods.append(m%t)
        newMods.append(mods)
    monkeyMods.append(newMods)
monkeys = monkeyMods
        
inspections = [0] * len(monkeys)
for i in range(10000):
    for j,monkey in enumerate(monkeys):
        inspections[j] += len(monkey)
        for val in monkey:
            if rhs[j] == 'old':
                for k,x in enumerate(val):
                    if ops[j] == '*':
                        val[k] = (val[k] * val[k]) % tests[k]
                    else:
                        val[k] = (val[k] + val[k]) % tests[k]
            else:
                r = int(rhs[j])
                for k,x in enumerate(val):
                    if ops[j] == '*':
                        val[k] = (val[k] * r) % tests[k]
                    else:
                        val[k] = (val[k] + r) % tests[k]
            if val[j] % tests[j] == 0:
                monkeys[true[j]].append(val)
            else:
                monkeys[false[j]].append(val)
        monkeys[j] = []
inspections.sort()
print(inspections[-2] * inspections[-1])