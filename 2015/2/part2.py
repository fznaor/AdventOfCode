file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
for line in lines:
    sides = [int(x) for x in line.strip().split('x')]
    sides.sort()
    res += 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]
print(res)