import re 
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()
times = []
records = []

for line in [line.strip() for line in lines]:
    line = re.sub(' +', '', line)
    if line.startswith('Time'):
        times = [int(x) for x in line.split(':')[1].strip().split()]
    else:
        records = [int(x) for x in line.split(':')[1].strip().split()]

res = []
for time,record in zip(times, records):
    count = 0
    for i in range(1, time):
        if (time - i) * i > record:
            count += 1
    res.append(count)
print(math.prod(res))