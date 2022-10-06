import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

num = []

for i, line in enumerate(lines):
    for item in num:
        item[1] += 1
    level = 1 if i > 0 else 0
    for c in line.rstrip():
        if(c == '['):
            level += 1
        elif(c == ']'):
            level -= 1
        elif(c == ','):
            continue
        else:
            num.append([int(c), level])
    
    if i == 0:
        continue
    
    while True:
        hasChanged = False
        for i in range(len(num)):
            if num[i][1] == 5:
                if i != 0:
                    num[i-1][0] += num[i][0]
                if i+2 < len(num):
                    num[i+2][0] += num[i+1][0]
                num[i] = [0, 4]
                num.pop(i+1)
                hasChanged = True
                break
        if not hasChanged:
            for i in range(len(num)):
                if num[i][0] >= 10:
                    a = math.floor(num[i][0]/2)
                    b = math.ceil(num[i][0]/2)
                    l = num[i][1]
                    num[i] = [a, l+1]
                    num.insert(i+1, [b, l+1])
                    hasChanged = True
                    break
        if not hasChanged:
            break
        
while True:
    maxLevel = max(num, key=lambda x: x[1])[1]
    for i,n in enumerate(num):
        if n[1] == maxLevel:
            n[0] = 3*num[i][0] + 2*num[i+1][0]
            n[1] -= 1
            num.pop(i+1)
            break
    if len(num) == 1:
        break
print(num[0][0])