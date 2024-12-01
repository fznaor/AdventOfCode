file1 = open('input.txt', 'r')
lines = file1.readlines()

visited = {}

records = []
damagedCounts = []
for line in [line.strip() for line in lines]:
    record = [x for x in line.split()[0]]
    recordToInsert = record.copy()
    for i in range(4):
        recordToInsert.append('?')
        recordToInsert.extend(record)
    records.append(recordToInsert)

    damagedCount = [int(x) for x in line.split()[1].split(',')]
    damagedCountToInsert = damagedCount.copy()
    for i in range(4):
        damagedCountToInsert.extend(damagedCount)
    damagedCounts.append(damagedCountToInsert)

def isValid(record, damagedCount, damageToInsert):
    if damageToInsert > record.count('?'):
        return False
    
    completedGroups = []
    groupActive = False
    currentGroupSize = 0
    for r in record:
        if r == '?':
            break
        if r == '#':
            if not groupActive:
                groupActive = True
                currentGroupSize = 1
            else:
                currentGroupSize += 1
        else:
            if groupActive:
                groupActive = False
                completedGroups.append(currentGroupSize)
                currentGroupSize = 0
    if len(completedGroups) > len(damagedCount):
        return False
    for i in range(len(completedGroups)):
        if completedGroups[i] != damagedCount[i]:
            return False
    if groupActive:
        if len(completedGroups) + 1 > len(damagedCount) or currentGroupSize > damagedCount[len(completedGroups)]:
            return False
    return True

def combination(record, damagedCount, i, damageToInsert):
    global visited
    if not isValid(record, damagedCount, damageToInsert):
        return 0
    while i < len(record) and record[i] != '?':
        i += 1
    if i >= len(record):
        return 1
    
    currState = []
    currStreak = 0
    isActive = False
    for ii in range(i):
        if record[ii] == '#':
            if isActive:
                currStreak += 1
            else:
                currStreak = 1
                isActive = True
        else:
            if isActive:
                currState.append(currStreak)
                isActive = False
    if (i, damageToInsert, tuple(currState), currStreak, isActive) in visited:
        return visited[(i, damageToInsert, tuple(currState), currStreak, isActive)]

    newRecord1 = record.copy()
    newRecord1[i] = '.'
    newRecord2 = record.copy()
    newRecord2[i] = '#'
    res = combination(newRecord1, damagedCount, i, damageToInsert) + combination(newRecord2, damagedCount, i, damageToInsert - 1)
    visited[(i, damageToInsert, tuple(currState), currStreak, isActive)] = res
    return res

s = 0
for record, damagedCount in zip(records, damagedCounts):
    s += combination(record, damagedCount, 0, sum(damagedCount) - record.count('#'))
    visited = {}
print(s)