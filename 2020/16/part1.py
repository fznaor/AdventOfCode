file1 = open('input.txt', 'r')
lines = file1.readlines()

allowedVals = []
res = 0
phase = 'f'
for line in lines:
    if phase == 'f':
        if len(line.rstrip()) == 0:
            allowedVals = list(set(allowedVals))
            phase = 's'
        else:
            a = line.rstrip().split(': ')[1]
            nums = a.split(' or ')
            [lolo, lohi] = [int(a) for a in nums[0].split('-')]
            [hilo, hihi] = [int(a) for a in nums[1].split('-')]
            allowedVals.extend(range(lolo, lohi + 1))
            allowedVals.extend(range(hilo, hihi + 1))
    elif phase == 's':
        if len(line.rstrip()) == 0:
            phase = 't'
        else:
            if not line.startswith('your'):
                myTicket = [int(a) for a in line.rstrip().split(',')]
    else:
        if not line.startswith('nearby'):
            ticket = [int(a) for a in line.rstrip().split(',')]
            for num in ticket:
                if num not in allowedVals:
                    res += num
print(res)