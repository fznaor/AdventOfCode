file1 = open('input.txt', 'r')
lines = file1.readlines()

mask = None
oneMask = 0
zeroMask = 0
mem = {}

for line in lines:
    if line.startswith('mask'):
        oneMask = 0
        zeroMask = 0
        mask = line.rstrip().split(' = ')[1]
        for i in range(len(mask)):
            if mask[i] == '1':
                oneMask = oneMask | (1 << (len(mask)-i-1))
            elif mask[i] == '0':
                zeroMask = zeroMask | (1 << (len(mask)-i-1))
    else:
        index = line.rstrip().split('[')[1].split(']')[0]
        value = int(line.rstrip().split('= ')[1])
        value = value | oneMask
        value = value & (~zeroMask)
        mem[index] = value

print(sum(mem.values()))     