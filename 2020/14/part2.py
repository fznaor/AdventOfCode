import itertools

file1 = open('input.txt', 'r')
lines = file1.readlines()

mask = None
oneMask = 0
zeroMask = 0
xIndices = []
mem = {}

for line in lines:
    if line.startswith('mask'):
        oneMask = 0
        zeroMask = 0
        xIndices = []
        mask = line.rstrip().split(' = ')[1]
        for i in range(len(mask)):
            if mask[i] == '1':
                oneMask = oneMask | (1 << (len(mask)-i-1))
            elif mask[i] == '0':
                zeroMask = zeroMask | (1 << (len(mask)-i-1))
            else:
                xIndices.append(len(mask)-i-1)
    else:
        index = int(line.rstrip().split('[')[1].split(']')[0])
        index = index | oneMask
        combs = itertools.product([True, False], repeat=len(xIndices))
        for comb in combs:
            currIndex = index
            value = int(line.rstrip().split('= ')[1])
            for i in range(len(xIndices)):
                if comb[i]:
                    currIndex = currIndex | (1 << (xIndices[i]))
                else:
                    currIndex = currIndex & ~(1 << (xIndices[i]))
            mem[currIndex] = value

print(sum(mem.values()))     