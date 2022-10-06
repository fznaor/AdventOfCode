from functools import reduce

file1 = open('input.txt', 'r')
lines = file1.readlines()

target = int(lines[0].rstrip())
vals = lines[1].rstrip().split(',')

divisors = []
mods = []

for i in range(len(vals)-1,-1,-1):
    if vals[i] == 'x':
        continue
    divisors.append(int(vals[i]))
    mods.append((len(vals)-1-i) % int(vals[i]))
    
m = reduce((lambda x, y: x * y), divisors)

def inv(a, m) :
    m0 = m
    x0 = 0
    x1 = 1
    if (m == 1) :
        return 0
    while (a > 1) :
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    # Make x1 positive
    if (x1 < 0) :
        x1 = x1 + m0
    return x1

res = 0

for i in range(len(divisors)):
    z = m // divisors[i]
    res += z * mods[i] * inv(z, divisors[i])
    
print((res % m) - len(vals) + 1)