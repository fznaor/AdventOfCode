import copy
import collections

file1 = open('v21.txt', 'r')
lines = file1.readlines()
paths = {}

res = 0

for line in lines:
    caves = line.rstrip().split('-')
    if caves[0] not in paths:
        paths[caves[0]] = [caves[1]]
    else:
        paths[caves[0]].append(caves[1])
    if caves[1] not in paths:
        paths[caves[1]] = [caves[0]]
    else:
        paths[caves[1]].append(caves[0])
        
def visit(cave, path):
    global res
    if cave == 'start' and path != []:
        return
    newpath = copy.deepcopy(path)
    if cave == 'end':
        newpath.append('end')
        res += 1
        return
    if cave not in paths:
        return
    newpath.append(cave)
    coll = collections.Counter(newpath)
    multiples = 0
    for key in coll.keys():
        if key.islower() and coll[key] == 2:
            multiples += 1
        if key.islower() and coll[key] > 2:
            return
    if multiples > 1:
        return
    for c in paths[cave]:
        visit(c, newpath)

visit('start', [])
print(res)