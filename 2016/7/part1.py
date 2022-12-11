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
    
    hasABBAoutsideBrackets = False
    hasABBAinsideBrackets = False
    for i,part in enumerate(line):
        if i % 2 == 0 and not hasABBAoutsideBrackets:
            if containsABBA(part):
                hasABBAoutsideBrackets = True
        elif i % 2 == 1 and not hasABBAinsideBrackets:
            if containsABBA(part):
                hasABBAinsideBrackets = True
    if hasABBAoutsideBrackets and not hasABBAinsideBrackets:
        res += 1
print(res)