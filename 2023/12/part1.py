file1 = open('input.txt', 'r')
lines = file1.readlines()

records = []
damagedCounts = []
for line in [line.strip() for line in lines]:
    records.append([x for x in line.split()[0]])
    damagedCounts.append([int(x) for x in line.split()[1].split(',')])

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
    if not isValid(record, damagedCount, damageToInsert):
        return 0
    while i < len(record) and record[i] != '?':
        i += 1
    if i >= len(record):
        return 1
    
    newRecord1 = record.copy()
    newRecord1[i] = '.'
    newRecord2 = record.copy()
    newRecord2[i] = '#'
    return combination(newRecord1, damagedCount, i, damageToInsert) + combination(newRecord2, damagedCount, i, damageToInsert - 1)

s = 0
for record, damagedCount in zip(records, damagedCounts):
    s += combination(record, damagedCount, 0, sum(damagedCount) - record.count('#'))
print(s)