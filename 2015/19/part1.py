file1 = open('input.txt', 'r')
lines = file1.readlines()

rules = dict()
firstPart = True
newStrings = []
for line in [line.strip() for line in lines]:
    if len(line) == 0:
        firstPart = False
        continue
    if firstPart:
        line = line.split(' ')
        if line[0] not in rules:
            rules[line[0]] = [line[2]]
        else:
            rules[line[0]].append(line[2])
    else:
        target = line

for key in rules:
    for i in range(len(target) - (len(key)-1)):
        if target[i:i+len(key)] == key:
            for rule in rules[key]:
                newStrings.append(target[:i] + rule + target[i+len(key):])
print(len(set(newStrings)))