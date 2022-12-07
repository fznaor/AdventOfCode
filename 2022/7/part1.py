file1 = open('input.txt', 'r')
lines = file1.readlines()

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

sizeLimit = 100000
sizeSum = 0
for d in dirTree:
    ds = dirSize(d)
    if(ds <= sizeLimit):
        sizeSum += ds
print(sizeSum)