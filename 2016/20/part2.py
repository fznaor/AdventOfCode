file1 = open('input.txt', 'r')
lines = file1.readlines()

ranges = []
minVal = 0

def findNextStart(ranges, val):
    minStart = 4294967295
    for [lo,hi] in ranges:
        if lo > val and lo < minStart:
            minStart = lo
    return minStart

for line in [line.strip() for line in lines]:
    [lo,hi] = [int(x) for x in line.split('-')]
    if lo == 0:
        minVal = hi + 1
    ranges.append([lo,hi])

count = 0
while True:
    hasChanged = False
    for [lo,hi] in ranges:
        if minVal in range(lo,hi+1):
            minVal = hi + 1
            hasChanged = True
    if not hasChanged:
        nextMinVal = findNextStart(ranges, minVal)
        if nextMinVal == 4294967295:
            print(count)
            break
        count += nextMinVal - minVal
        minVal = nextMinVal