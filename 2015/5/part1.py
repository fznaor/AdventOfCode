def isNice(s):
    if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') < 3:
        return False
    repeats = False
    for i,x in enumerate(s[:-1]):
        if s[i] == s[i+1]:
            repeats = True
    if not repeats:
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True

file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
for line in lines:
    if isNice(line.strip()):
        res += 1
print(res)