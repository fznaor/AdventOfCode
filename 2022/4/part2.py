file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    pairs = line.strip().split(',')
    first = [int(x) for x in pairs[0].split('-')]
    second = [int(x) for x in pairs[1].split('-')]
    if (first[0] <= second[1] and second[0] <= first[1]):
        count += 1
print(count)