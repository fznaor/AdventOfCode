file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
sums = []
for line in lines:
    if len(line.strip()) == 0:
        sums.append(s)
        s = 0
    else:
        s += int(line.strip())
sums.sort()
print(sum(sums[-3:]))