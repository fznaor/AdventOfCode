file1 = open('input.txt', 'r')
lines = file1.readlines()

vals = {'a': 0, 'b': 0}
lines = [line.strip().split(' ') for line in lines]

i = 0
while True:
    if i not in range(len(lines)):
        break
    line = lines[i]
    if line[0] == 'hlf':
        vals[line[1]] /= 2
        i += 1
    elif line[0] == 'tpl':
        vals[line[1]] *= 3
        i += 1
    elif line[0] == 'inc':
        vals[line[1]] += 1
        i += 1
    elif line[0] == 'jmp':
        if line[1][0] == '+':
            i += int(line[1][1:])
        else:
            i -= int(line[1][1:])
    elif line[0] == 'jie':
        if int(vals[line[1][:-1]]) % 2 == 0:
            if line[2][0] == '+':
                i += int(line[2][1:])
            else:
                i -= int(line[2][1:])
        else:
            i += 1
    elif line[0] == 'jio':
        if int(vals[line[1][:-1]]) == 1:
            if line[2][0] == '+':
                i += int(line[2][1:])
            else:
                i -= int(line[2][1:])
        else:
            i += 1
print(vals['b'])