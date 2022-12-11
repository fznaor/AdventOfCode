file1 = open('input.txt', 'r')
lines = file1.readlines()

i = 0
j = 0
drctn = 0 #nesw
vals = lines[0].strip().split(', ')
for val in vals:
    [d,n] = [val[0], int(val[1:])]
    if d == 'R':
        drctn += 1
    else:
        drctn -= 1
    drctn %= 4
    if drctn == 0:
        i -= n
    elif drctn == 1:
        j += n
    elif drctn == 2:
        i += n
    else:
        j -= n
print(abs(i)+abs(j))