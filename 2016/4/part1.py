file1 = open('input.txt', 'r')
lines = file1.readlines()

def sort_key(item):
    key, value = item
    return -value, key

count = 0
for line in lines:
    occurences = dict()
    [code,checksum] = line.split('[')
    roomId = int(code.split('-')[-1])
    checksum = checksum[:-1]
    
    for c in code:
        if c.islower():
            if c not in occurences:
                occurences[c] = 1
            else:
                occurences[c] += 1
                
    isReal = True
    srtd = dict(sorted(occurences.items(), key=sort_key))
    for i,key in enumerate(srtd):
        if i == 5:
            break
        if not key in checksum:
            isReal = False
            break
    if isReal:
        count += roomId
print(count)