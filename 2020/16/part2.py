file1 = open('input.txt', 'r')
lines = file1.readlines()

allowedVals = []
av = {}
tickets = []
possibleKeys = {}
certainKeys = []
phase = 'f'
for line in lines:
    if phase == 'f':
        if len(line.rstrip()) == 0:
            allowedVals = list(set(allowedVals))
            phase = 's'
        else:
            category = line.rstrip().split(': ')[0]
            a = line.rstrip().split(': ')[1]
            nums = a.split(' or ')
            [lolo, lohi] = [int(a) for a in nums[0].split('-')]
            [hilo, hihi] = [int(a) for a in nums[1].split('-')]
            allowedVals.extend(range(lolo, lohi + 1))
            allowedVals.extend(range(hilo, hihi + 1))
            av[category] = []
            av[category].extend(range(lolo, lohi + 1))
            av[category].extend(range(hilo, hihi + 1))
    elif phase == 's':
        if len(line.rstrip()) == 0:
            phase = 't'
        else:
            if not line.startswith('your'):
                myTicket = [int(a) for a in line.rstrip().split(',')]
    else:
        if not line.startswith('nearby'):
            ticket = [int(a) for a in line.rstrip().split(',')]
            valid = True
            for num in ticket:
                if num not in allowedVals:
                    valid = False
            if valid:
                tickets.append(ticket)
for i in range(len(av)):
    possibleKeys[str(i)] = []
    for key in av:
        if key in certainKeys:
            continue
        valid = True
        for ticket in tickets:
            if ticket[i] not in av[key]:
                valid = False
                break
        if myTicket[i] not in av[key]:
            valid = False
        if valid:
            possibleKeys[str(i)].append(key)

res = ' '.join(sorted(possibleKeys, key = lambda key: len(possibleKeys[key])))
order = [int(i) for i in res.split(' ')]

product = 1
for i in order:
    for x in possibleKeys[str(i)]:
        if x not in certainKeys:
            certainKeys.append(x)
            if 'departure' in x:
                product *= myTicket[i]
            break
print(product)