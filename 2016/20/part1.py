file1 = open('input.txt', 'r')
lines = file1.readlines()

ranges = []
minVal = 0

for line in [line.strip() for line in lines]:
    [lo,hi] = [int(x) for x in line.split('-')]
    if lo == 0:
        minVal = hi + 1
    ranges.append([lo,hi])

while True:
    hasChanged = False
    for [lo,hi] in ranges:
        if minVal in range(lo,hi+1):
            minVal = hi + 1
            hasChanged = True
    if not hasChanged:
        print(minVal)
        break