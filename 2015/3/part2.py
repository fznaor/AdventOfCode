file1 = open('input.txt', 'r')
lines = file1.readlines()

i1 = 0
j1 = 0
i2 = 0
j2 = 0
delivered = dict()
delivered[0,0] = 1
for ii,c in enumerate(lines[0].strip()):
    i = 0
    j = 0
    if c == '^':
        i = -1
    elif c == 'v':
        i = 1
    elif c == '>':
        j = 1
    elif c == '<':
        j = -1
    if ii % 2 == 0:
        i1 += i
        j1 += j
        [i,j] = [i1,j1]
    else:
        i2 += i
        j2 += j
        [i,j] = [i2,j2]
    if not (i,j) in delivered:
        delivered[i,j] = 1
    else:
        delivered[i,j] += 1
print(len(delivered))