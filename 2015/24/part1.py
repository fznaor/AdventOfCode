import numpy as np
import itertools
import math
from functools import reduce
file1 = open('input.txt', 'r')
lines = file1.readlines()

weights = []
for line in [line.strip() for line in lines]:
    weights.append(int(line))
weights = np.array(lines, np.int64)
totalSum = sum(weights)
solutions = []

for i in range(1,len(weights)-1):
    found = False
    for c in itertools.combinations(weights,i):
        if totalSum == 3*sum(c):
            unused = [w for w in weights if w not in c]
            for j in range(1,len(unused)-1):
                for q in itertools.combinations(unused,j):
                    if totalSum == 3*sum(q):
                        found = True
                        solutions.append(c)
                        break
            if found:
                break
    if found:
        break
solutions = list(set(solutions))
minProduct = math.inf
for s in solutions:
    pr = reduce((lambda x, y: x*y), s)
    if pr < minProduct:
        minProduct = pr
print(minProduct)