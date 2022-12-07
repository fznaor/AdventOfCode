import hashlib

inp = 'yzbqklnj'

i = 1
while True:
    h = hashlib.md5((inp + str(i)).encode('utf-8')).hexdigest()
    if h.startswith('000000'):
        print(i)
        break
    i += 1