def compareLists(a,b):
    for i in range(min([len(a),len(b)])):
        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] < b[i]:
                return 1
            if a[i] > b[i]:
                return 2
        else:
            if isinstance(a[i], int):
                a[i] = [a[i]]
            elif isinstance(b[i], int):
                b[i] = [b[i]]
            res = compareLists(a[i], b[i])
            if res in [1,2]:
                return res
    if len(a) < len(b):
        return 1
    if len(a) > len(b):
        return 2
    return 0

import ast
file1 = open('input.txt', 'r')
lines = file1.readlines()

num = 1
res = 0
for i,line in enumerate([line.strip() for line in lines]):
    if i % 3 == 2:
        num += 1
    elif i % 3 == 0:
        first = ast.literal_eval(line)
    elif i % 3 == 1:
        second = ast.literal_eval(line)
        if compareLists(first,second) == 1:
            res += num
print(res)