file1 = open('input.txt', 'r')
lines = file1.readlines()

rules = {}

for line in [line.strip() for line in lines]:
    if len(line) == 0:
        break
    
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

s = 0
def checkRule(rule, bounds):
    global s
    for condition in rules[rule]["conditions"]:
        newBounds = {}
        for key in bounds:
            newBounds[key] = bounds[key].copy()
        relevantVal = condition[0]
        compareTo = condition[2]
        biggerThan = True if condition[1] == '>' else False
        if biggerThan:
            newBounds[relevantVal][0] = compareTo + 1
            bounds[relevantVal][1] = compareTo
        else:
            newBounds[relevantVal][1] = compareTo - 1
            bounds[relevantVal][0] = compareTo
        if compareTo + 1 > 4000 or compareTo - 1 < 0:
            continue
        if newBounds[relevantVal][0] > newBounds[relevantVal][1]:
            continue
        newRule = condition[3]
        if newRule == 'A':
            prod = 1
            for key in newBounds:
                prod *= (newBounds[key][1] - newBounds[key][0] + 1)
            s += prod
            continue
        if newRule == 'R':
            continue
        checkRule(newRule, newBounds)
    lastRule = rules[rule]['otherwise']
    if lastRule == 'A':
        prod = 1
        for key in bounds:
            prod *= (bounds[key][1] - bounds[key][0] + 1)
        s += prod
        return
    if lastRule == 'R':
        return
    checkRule(lastRule, bounds)

bounds = {'x' : [1,4000], 'm':  [1,4000], 'a': [1,4000], 's': [1,4000]}
checkRule('in', bounds)
print(s)