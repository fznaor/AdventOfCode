file1 = open('input.txt', 'r')
lines = file1.readlines()

length = 0
for line in [line.strip() for line in lines]:
    i = 0
    while i < len(line):
        if line[i] == '(':
            i += 1
            toParse = ''
            while line[i] != ')':
                toParse += line[i]
                i += 1
            i += 1
            [size,times] = [int(x) for x in toParse.split('x')]
            length += size*times
            i += size
        else:
            length += 1
            i += 1
print(length)