file1 = open('input.txt', 'r')
lines = file1.readlines()
remainingLines = [x for x in range(len(lines))]

vals = dict()
while len(remainingLines) > 0:
    for i,line in enumerate(lines):
        if not i in remainingLines:
            continue
        line = line.strip().split(' ')
        if len(line) == 3:
            if line[0].isnumeric():
                vals[line[2]] = int(line[0])
                remainingLines.remove(i)
            elif not line[0] in vals:
                continue
            else:
                vals[line[2]] = vals[line[0]]
                remainingLines.remove(i)
        elif len(line) == 4:
            if not line[1] in vals:
                continue
            vals[line[3]] = vals[line[1]] ^ 0xFFFF
            remainingLines.remove(i)
        else:
            if line[1] == 'AND':
                if not line[2] in vals:
                    continue
                if line[0] == '1':
                    vals[line[4]] = 1 & vals[line[2]]
                    remainingLines.remove(i)
                else:
                    if not line[0] in vals:
                        continue
                    vals[line[4]] = vals[line[0]] & vals[line[2]]
                    remainingLines.remove(i)
            elif line[1] == 'OR':
                if not line[0] in vals or not line[2] in vals:
                    continue
                vals[line[4]] = vals[line[0]] | vals[line[2]]
                remainingLines.remove(i)
            elif line[1] == 'LSHIFT':
                if not line[0] in vals:
                    continue
                vals[line[4]] = vals[line[0]] << int(line[2])
                remainingLines.remove(i)
            elif line[1] == 'RSHIFT':
                if not line[0] in vals:
                    continue
                vals[line[4]] = vals[line[0]] >> int(line[2])
                remainingLines.remove(i)
print(vals['a'])