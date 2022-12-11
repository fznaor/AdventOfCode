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
    code = code[:-len(code.split('-')[-1])]
    
    toMove = roomId % 26
    res = ''
    for c in code:
        if c == '-':
            c = ' '
            res += c
        else:
            newC = ord(c) + toMove
            if newC > ord('z'):
                newC -= 26
            res += chr(newC)
    if res.startswith('northpole object storage'):
        print(roomId)
        break