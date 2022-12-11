doorId = "cxdnnyjw"
import hashlib

i = 0
found = 0
code = ['']*8
while True:
    h = hashlib.md5((doorId + str(i)).encode('utf-8')).hexdigest()
    if h.startswith('00000'):
        if h[5].isnumeric():
            if int(h[5]) < 8 and code[int(h[5])] == '':
                code[int(h[5])] = h[6]
                found += 1
        if found == 8:
            break
    i += 1
for c in code:
    print(c,end='')