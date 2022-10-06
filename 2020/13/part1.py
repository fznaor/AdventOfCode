import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

target = int(lines[0].rstrip())
vals = lines[1].rstrip().split(',')

minID = 0
minTime = math.inf

for val in vals:
    if val == 'x':
        continue
    if (target // int(val) + 1) * int(val) < minTime:
        minTime = (target // int(val) + 1) * int(val)
        minID = int(val)
        
print(minID * (minTime - target))