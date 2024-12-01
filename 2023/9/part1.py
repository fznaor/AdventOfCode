file1 = open('input.txt', 'r')
lines = file1.readlines()

def getVal(arr):
    allArrs = []
    allArrs.append(arr)
    i = 0
    while True:
        diffs = []
        for x,y in zip(allArrs[i][0:-1], allArrs[i][1:]):
            diffs.append(y-x)
        if not any(diffs):
            break
        allArrs.append(diffs)
        i += 1
    s = 0
    for ar in allArrs[-1::-1]:
        s += ar[-1]
    return s

s = 0
for line in [line.strip() for line in lines]:
    arr = [int(x) for x in line.split()]
    s += getVal(arr)
print(s)