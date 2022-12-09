file1 = open('input.txt', 'r')
lines = file1.readlines()
import random
rules = dict()
firstPart = True
for line in [line.strip() for line in lines]:
    if len(line) == 0:
        firstPart = False
        continue
    if firstPart:
        line = line.split(' ')
        if line[2] not in rules:
            rules[line[2]] = [line[0]]
        else:
            rules[line[2]].append(line[0])
    else:
        target = line

# stochastic search, may need multiple runs to print final result
keys = list(rules.keys())
random.shuffle(keys)
steps = 0
while True:
    found = False
    for key in keys:
        for i in range(len(target) - (len(key)-1)):
            if target[i:i+len(key)] == key:
                for rule in rules[key]:
                    steps += 1
                    target = target[:i] + rule + target[i+len(key):]
                    if target == 'e':
                        print(steps)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        break