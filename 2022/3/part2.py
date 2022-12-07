file1 = open('input.txt', 'r')
lines = file1.readlines()

score = 0
for numLine, line in enumerate(lines):
    line = line.strip()
    if numLine % 3 == 0:
        firstLine = set()
        secondLine = set()
        for c in line:
            firstLine.add(c)
    elif numLine % 3 == 1:
        for c in line:
            secondLine.add(c)
    else:
        for c in line:
            if (c in firstLine) and (c in secondLine):
                if c >= 'a' and c <= 'z':
                    score += ord(c) - 96
                else:
                    score += ord(c) - 38
                break
print(score)