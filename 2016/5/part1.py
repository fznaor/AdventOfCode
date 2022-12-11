doorId = "cxdnnyjw"
import hashlib

i = 0
code = ''
while True:
    h = hashlib.md5((doorId + str(i)).encode('utf-8')).hexdigest()
    if h.startswith('00000'):
        code += h[5]
        if len(code) == 8:
            break
    i += 1
print(code)