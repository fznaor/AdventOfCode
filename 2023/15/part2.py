file1 = open('input.txt', 'r')
lines = file1.readlines()

sequence = ""

positions = {}
values = {}

def getHash(n):
    x = 0
    for c in n:
        x += ord(c)
        x *= 17
        x %= 256
    return x

for line in [line.strip() for line in lines]:
    sequence += line

s = 0
for seg in sequence.split(','):
    if '=' in seg:
        val = seg.split('=')[0]
        h = getHash(val)
        if h not in positions:
            positions[h] = [val]
        else:
            if val not in positions[h]:
                positions[h].append(val)
        values[val] = int(seg.split('=')[1])
    else:
        val = seg[:-1]
        h = getHash(val)
        if h in positions and val in positions[h]:
            positions[h].remove(val)
        if val in values:
            del values[val]

s = 0
for key in positions:
    for i,item in enumerate(positions[key]):
        s += (key + 1) * (i + 1) * values[item]
print(s)