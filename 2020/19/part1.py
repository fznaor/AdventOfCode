import numpy as np

file1 = open('input.txt', 'r')
lines = file1.readlines()

rules = {}
words = []
aIdx = []
bIdx = []
readingRules = True
testWords = []

for line in lines:
    if len(line.rstrip()) == 0:
        readingRules = False
        continue
        
    if readingRules:
        line = line.rstrip()
        idx, rest = line.split(':')
        idx = int(idx)
        
        rest = rest.split('|')
        
        try:
            first = [int(i) for i in rest[0].strip().split(' ')]
            if len(rest) == 2:
                second = [int(i) for i in rest[1].strip().split(' ')]
                rules[idx] = [first, second]
            else:
                rules[idx] = [first]
        except:
            for r in rest:
                letter = r.split('"')[1]
                if letter == 'a':
                    aIdx.append(idx)
                else:
                    bIdx.append(idx)
    else:
        testWords.append(line.rstrip())

count = 0
for ii,word in enumerate(testWords):
    print(ii, len(testWords))
    exist = np.full((len(word)+1, len(word)+1, max(rules)+1), False)
    for i in range(len(word)):
        if word[i] == 'a':
            for j in aIdx:
                exist[1,i+1,j] = True
        else:
            for j in bIdx:
                exist[1,i+1,j] = True
    for l in range(2,len(word)+1):
        for s in range(1,len(word)-l+2):
            for p in range(1,l):
                for key in rules:
                    for subrule in rules[key]:
                        if exist[p,s,subrule[0]] and exist[l-p,s+p,subrule[1]]:
                            exist[l,s,key] = True
    if exist[len(word),1,0]:
        count += 1
print(count)