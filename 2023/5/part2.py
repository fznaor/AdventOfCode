import re 

seedRanges = []
seeds = []
rules = []

file1 = open('input.txt', 'r')
lines = file1.readlines()
skipNextLine = False
startNewRule = True
for line in [line.strip() for line in lines]:
    line = re.sub(' +', ' ', line)
    if skipNextLine:
        skipNextLine = False
        startNewRule = True
        continue
    if(len(line) == 0):
        skipNextLine = True
        continue
    if(line.startswith("seeds:")):
        seedRanges = [int(x) for x in line.split(':')[1].strip().split()]
    elif startNewRule:
        rules.append([[int(x) for x in line.split()]])
        startNewRule = False
    else:
        rules[-1].append([int(x) for x in line.split()])

i = 1
found = False
while True:
    val = i
    for ruleSet in rules[::-1]:
        for [d,s,l] in ruleSet:
            if val >= d and val <= d + l:
                offset = val - d
                val = s + offset
                break
    for x,y in zip(seedRanges[::2], seedRanges[1::2]):
        if val in range(x,x+y):
            print(i)
            found = True
            break
    if found:
        break
    i += 1