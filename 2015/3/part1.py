file1 = open('input.txt', 'r')
lines = file1.readlines()

i = 0
j = 0
delivered = dict()
delivered[0,0] = 1
for c in lines[0].strip():
    if c == '^':
        i -= 1
    elif c == 'v':
        i += 1
    elif c == '>':
        j += 1
    elif c == '<':
        j -= 1
    if not (i,j) in delivered:
        delivered[i,j] = 1
    else:
        delivered[i,j] += 1
print(len(delivered))