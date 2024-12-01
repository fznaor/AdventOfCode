import re 

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
        seeds = [int(x) for x in line.split(':')[1].strip().split()]
    elif startNewRule:
        rules.append([[int(x) for x in line.split()]])
        startNewRule = False
    else:
        rules[-1].append([int(x) for x in line.split()])

for i,seed in enumerate(seeds):
    for ruleSet in rules:
        for [d,s,l] in ruleSet:
            if seed >= s and seed <= s + l:
                offset = seed - s
                seed = d + offset
                break
    seeds[i] = seed
print(min(seeds))