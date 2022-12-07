def isNice(s):
    repeats = False
    for i,x in enumerate(s[:-2]):
        if s[i] == s[i+2]:
            repeats = True
    if not repeats:
        return False
    
    repeats = False
    for i,x in enumerate(s[:-1]):
        for j,y in enumerate(s[:-1]):
            if not j in range(i-1,i+2):
                if s[i:i+2] == s[j:j+2]:
                    repeats = True
    return repeats

file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
for line in lines:
    if isNice(line.strip()):
        res += 1
print(res)