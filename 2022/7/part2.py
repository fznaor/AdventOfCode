file1 = open('input.txt', 'r')
lines = file1.readlines()
import math

def dirSize(d):
    size = dirTree[str(d)]['size']
    for child in dirTree[str(d)]['children']:
        size += dirSize(child)
    return size

currentDir = ['/']
dirTree = dict()
dirTree[str(currentDir)] = dict()
dirTree[str(currentDir)]['size'] = 0
dirTree[str(currentDir)]['children'] = []
for line in [line.strip().split(' ') for line in lines]:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                continue
            if line[2] == '..':
                currentDir = currentDir[:-1]
            else:
                currentDir.append(line[2])
                dirTree[str(currentDir)] = dict()
                dirTree[str(currentDir)]['size'] = 0
                dirTree[str(currentDir)]['children'] = []
    elif line[0][0].isdigit():
        dirTree[str(currentDir)]['size'] += int(line[0])
    else:
        dirTree[str(currentDir)]['children'].append(currentDir+[line[1]])

toDelete = 30000000 - (70000000 - dirSize(['/']))
minToDelete = math.inf
for d in dirTree:
    ds = dirSize(d)
    if ds >= toDelete and ds < minToDelete:
        minToDelete = ds
print(minToDelete)