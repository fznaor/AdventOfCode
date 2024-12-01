import re 

file1 = open('input.txt', 'r')
lines = file1.readlines()
counter = [1] * len(lines)

for i,line in enumerate([line.strip() for line in lines]):
    line = re.sub(' +', ' ', line)
    winningNums = [int(val) for val in line.split(': ')[1].split('|')[0].strip().split(' ')]
    myNums = [int(val) for val in line.split(': ')[1].split('|')[1].strip().split(' ')]

    matches = 0
    for num in myNums:
        if num in winningNums:
            matches += 1
    if matches > 0:
        for j in range(i+1, i+1+matches):
            counter[j] += counter[i]

print(sum(counter))