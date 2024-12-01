file1 = open('input.txt', 'r')
lines = file1.readlines()

firsts = []
seconds = []

for line in lines:
    [f,s] = [int(x) for x in line.strip().split()]
    firsts.append(f)
    seconds.append(s)

firsts.sort()
seconds.sort()

res = 0
for (f,s) in zip(firsts, seconds):
    res += abs(f-s)

print(res)