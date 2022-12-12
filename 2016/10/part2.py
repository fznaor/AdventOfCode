file1 = open('input.txt', 'r')
lines = file1.readlines()

bots = dict()
outputs = dict()
executedLines = []

while len(executedLines) < len(lines):
    for i,line in enumerate([line.strip().split(' ') for line in lines]):
        if line[0].startswith('value') and not i in executedLines:
            executedLines.append(i)
            if not int(line[-1]) in bots:
                bots[int(line[-1])] = [int(line[1])]
            else:
                bots[int(line[-1])].append(int(line[1]))
        elif not i in executedLines:
            giver = int(line[1])
            if giver not in bots:
                continue
            if len(bots[giver]) != 2:
                continue
            executedLines.append(i)
            [lo,hi] = sorted(bots[giver])
            if line[5] == 'bot':
                if not int(line[6]) in bots:
                    bots[int(line[6])] = [lo]
                else:
                    bots[int(line[6])].append(lo)
                bots[giver].remove(lo)
            else:
                if not int(line[6]) in outputs:
                    outputs[int(line[6])] = [lo]
                else:
                    outputs[int(line[6])].append(lo)
                bots[giver].remove(lo)
                
            if line[10] == 'bot':
                if not int(line[11]) in bots:
                    bots[int(line[11])] = [hi]
                else:
                    bots[int(line[11])].append(hi)
                bots[giver].remove(hi)
            else:
                if not int(line[11]) in outputs:
                    outputs[int(line[11])] = [hi]
                else:
                    outputs[int(line[11])].append(hi)
                bots[giver].remove(hi)
                
print(outputs[0][0]*outputs[1][0]*outputs[2][0])