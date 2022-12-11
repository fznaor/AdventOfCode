file1 = open('input.txt', 'r')
lines = file1.readlines()

def containsABBA(s):
    for i in range(len(s)-3):
        [a,b,c,d] = s[i:i+4]
        if d == a and b == c and a != c:
            return True
    return False

res = 0
for line in [line.strip() for line in lines]:
    line = line.replace(']', '[')
    line = line.split('[')
    
    out = []
    ins = []
    
    for i,x in enumerate(line):
        if i % 2 == 0:
            out.append(x)
        else:
            ins.append(x)
    
    found = False
    for o in out:
        for i in range(len(o) - 2):
            [a,b,c] = o[i:i+3]
            test = b+a+b
            if a != b and a == c:
                for x in ins:
                    if test in x:
                        found = True
                        break
            if found:
                break
        if found:
            break
    if found:
        res += 1
print(res)