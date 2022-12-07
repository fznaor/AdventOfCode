file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    pairs = line.strip().split(',')
    first = [int(x) for x in pairs[0].split('-')]
    second = [int(x) for x in pairs[1].split('-')]
    if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):
        count += 1
print(count)