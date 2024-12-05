file1 = open('input.txt', 'r')
lines = file1.readlines()

rules = []
res = 0

firstPart = True
for line in [line.strip() for line in lines]:
    if(len(line) == 0):
        firstPart = False
        continue
    if firstPart:
        x,y = [int(a) for a in line.split('|')]
        rules.append((x,y))
    else:
        lineVals = [int(x) for x in line.split(',')]
        valid = True
        for x,y in rules:
            if x in lineVals and y in lineVals and lineVals.index(x) > lineVals.index(y):
                valid = False
                break
        if not valid:
            while True:
                cleanPass = True
                for x,y in rules:
                    if x in lineVals and y in lineVals:
                        xi = lineVals.index(x)
                        yi = lineVals.index(y)
                        if xi > yi:
                            cleanPass = False
                            lineVals[xi] = y
                            lineVals[yi] = x
                if cleanPass:
                    break
            res += lineVals[len(lineVals) // 2]
print(res)