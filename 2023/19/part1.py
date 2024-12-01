file1 = open('input.txt', 'r')
lines = file1.readlines()

rules = {}
readingRules = True
vals = []

for line in [line.strip() for line in lines]:
    if len(line) == 0:
        readingRules = False
        continue
    
    if readingRules:
        ruleName = line.split('{')[0]
        rules[ruleName] = {}
        rules[ruleName]["conditions"] = []
        body = line.split('{')[1][:-1]
        for part in body.split(','):
            if ':' in part:
                part1 = part.split(':')[0]
                part2 = part.split(':')[1]
                rules[ruleName]["conditions"].append(([part1[0], part1[1], int(part1[2:]), part2]))
            else:
                rules[ruleName]["otherwise"] = part

    else:
        newDict = {}
        for part in line[1:-1].split(','):
            newDict[part[0]] = int(part[2:])
        vals.append(newDict)

s = 0
for val in vals:
    workflow = 'in'
    while True:
        found = False
        foundExit = False
        for condition in rules[workflow]["conditions"]:
            relevantVal = val[condition[0]]
            compareTo = condition[2]
            if condition[1] == '>':
                if relevantVal > compareTo:
                    workflow = condition[3]
                    if workflow == 'A' :
                        for x in val:
                            s += val[x]
                        foundExit = True
                        break
                    if workflow == 'R' :
                        foundExit = True
                        break
                    found = True
                    break
            else:
                if relevantVal < compareTo:
                    workflow = condition[3]
                    if workflow == 'A' :
                        for x in val:
                            s += val[x]
                        foundExit = True
                        break
                    if workflow == 'R' :
                        foundExit = True
                        break
                    found = True
                    break
        if foundExit:
            break
        if not found:
            workflow = rules[workflow]['otherwise']
            if workflow == 'A' :
                for x in val:
                    s += val[x]
                foundExit = True
                break
            if workflow == 'R' :
                foundExit = True
                break
print(s)