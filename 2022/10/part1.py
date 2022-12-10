file1 = open('input.txt', 'r')
lines = file1.readlines()

cycle = 0
x = 1
res = 0
for line in [line.strip().split(' ') for line in lines]:
    if line[0] == "noop":
        cycle += 1
        if cycle in range(20,221,40):
            res += cycle * x
    else:
        cycle += 2
        if cycle-1 in range(20,221,40):
            res += (cycle-1) * x
        if cycle in range(20,221,40):
            res += cycle * x
        x += int(line[1])
print(res)