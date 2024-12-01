file1 = open('input.txt', 'r')
lines = file1.readlines()

firsts = []
seconds = []

for line in lines:
    [f,s] = [int(x) for x in line.strip().split()]
    firsts.append(f)
    seconds.append(s)

res = 0
for f in firsts:
    res += f * seconds.count(f)

print(res)