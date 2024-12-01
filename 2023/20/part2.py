file1 = open('input.txt', 'r')
lines = file1.readlines()

modules = {}

for line in [line.strip() for line in lines]:
    parts = line.split(' -> ')
    
    if 'broadcaster' in line:
        broadcaster = [x for x in parts[1].split(', ')]
    elif '%' in line:
        modules[parts[0][1:]] = [True, False, [x for x in parts[1].split(', ')]] # is toggle, current status
    else:
        modules[parts[0][1:]] = [False, [x for x in parts[1].split(', ')], {}] # is conjunction

for entry in modules:
    if not modules[entry][0]:
        for entry2 in modules:
            if modules[entry2][0]:
                if entry in modules[entry2][2]:
                    modules[entry][2][entry2] = False

i = 0
cyclesFound = 0
s = 1
found = False
while True:
    i += 1
    queue = []
    for item in broadcaster:
        queue.append((item, False, ''))
    while len(queue) > 0:
        item, isHigh, caller = queue.pop(0)
        if item not in modules:
            continue
        if modules[item][0]: # toggle
            if isHigh:
                continue
            modules[item][1] = not modules[item][1]
            for x in modules[item][2]:
                queue.append((x, modules[item][1], item))
        else:
            remembered = modules[item][2]
            remembered[caller] = isHigh

            onlyHiStates = True
            for entry in remembered:
                if not remembered[entry]:
                    onlyHiStates = False
                    break

            if item == 'kr' and not onlyHiStates:
                s *= i
                cyclesFound += 1
                if cyclesFound == 4:
                    print(s)
                    found = True
            if item == 'zs' and not onlyHiStates:
                s *= i
                cyclesFound += 1
                if cyclesFound == 4:
                    print(s)
                    found = True
            if item == 'kf' and not onlyHiStates:
                s *= i
                cyclesFound += 1
                if cyclesFound == 4:
                    print(s)
                    found = True
            if item == 'qk' and not onlyHiStates:
                s *= i
                cyclesFound += 1
                if cyclesFound == 4:
                    print(s)
                    found = True
            if found:
                break
           
            for x in modules[item][1]:
                queue.append((x, not onlyHiStates, item))
    if found:
        break