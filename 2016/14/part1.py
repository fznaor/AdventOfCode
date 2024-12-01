import hashlib

salt = 'qzyelonm'
i = 1
foundKeys = 0
hashes = {}

while True:
    found = False
    if i in hashes:
        hash = hashes[i]
    else:
        hash = hashlib.md5((salt + str(i)).encode('utf-8')).hexdigest()
        hashes[i] = hash
    tripletFound = False
    for [a,b,c] in zip(hash[:-2],hash[1:-1],hash[2:]):
        if a == b == c:
            tripletFound = True
            for j in range(i+1, i+1001):
                if j in hashes:
                    newHash = hashes[j]
                else:
                    newHash = hashlib.md5((salt + str(j)).encode('utf-8')).hexdigest()
                    hashes[j] = newHash
                for [d,e,f,g,h] in zip(newHash[:-4],newHash[1:-3],newHash[2:-2],newHash[3:-1],newHash[4:]):
                    if d == e == f == g == h == b:
                        foundKeys += 1
                        found = True
                        break
            if found or tripletFound:
                break
        if found:
            break
    if found:
        if foundKeys == 64:
            print(i)
            break
    i += 1