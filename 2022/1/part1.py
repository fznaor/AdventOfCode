file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
maxS = 0
for line in lines:
    if len(line.strip()) == 0:
        if s > maxS:
            maxS = s
        s = 0
    else:
        s += int(line.strip())
print(maxS if maxS > s else s)