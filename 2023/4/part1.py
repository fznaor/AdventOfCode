import re 

file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
for line in [line.strip() for line in lines]:
    line = re.sub(' +', ' ', line)
    winningNums = [int(val) for val in line.split(': ')[1].split('|')[0].strip().split(' ')]
    myNums = [int(val) for val in line.split(': ')[1].split('|')[1].strip().split(' ')]

    matches = 0
    for num in myNums:
        if num in winningNums:
            matches += 1
    if matches > 0:
        s += 2 ** (matches - 1)
print(s)