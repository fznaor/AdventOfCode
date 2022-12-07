file1 = open('input.txt', 'r')
lines = file1.readlines()

stacks = dict()
for line in lines:
    if not line.startswith('move'):
        for i,l in enumerate(line):
            if i % 4 == 1 and 'A' <= line[i] <= 'Z':
                index = i//4 + 1
                if not index in stacks:
                    stacks[index] = [line[i]]
                else:
                    stacks[index].insert(0, line[i])
    else:
        parts = line.strip().split(' ')
        quantity = int(parts[1])
        start = int(parts[3])
        end = int(parts[5])
        for j in range(quantity):
            stacks[end].append(stacks[start].pop())
for i in sorted(stacks):
    print(stacks[i][-1], end='')
    