file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
for line in [line.strip() for line in lines]:
    p = 1
    num = 0
    for x in line[-1::-1]:
        if x.isnumeric():
            xx = int(x)
        elif x == '-':
            xx = -1
        elif x == '=':
            xx = -2
        num += xx*p
        p *= 5
    s += num

res = ''
while s != 0:
    r = s % 5
    s //= 5
    if r < 3:
        res = str(r) + res
    elif r == 3:
        res = '=' + res
        s += 1
    else:
        res = '-' + res
        s += 1
print(res)