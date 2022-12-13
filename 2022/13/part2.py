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

vals = []
for i,line in enumerate([line.strip() for line in lines]):
    if i % 3 != 2:
        vals.append(ast.literal_eval(line))
vals.append([[2]])
vals.append([[6]])

sortedVals = []
firstInsert = 0
secondInsert = 0
for i in range(len(vals)):
    if len(sortedVals) == 0:
        sortedVals.append(vals[i])
    else:
        inserted = False
        for j in range(len(sortedVals)):
            if compareLists(vals[i],sortedVals[j]) == 1:
                sortedVals.insert(j,vals[i])
                inserted = True
                if i == len(vals) - 2:
                    firstInsert = j + 1
                elif i == len(vals) - 1:
                    secondInsert = j + 1
                    if secondInsert <= firstInsert:
                        firstInsert += 1
                break
        if not inserted:
            sortedVals.append(vals[i])
print(firstInsert*secondInsert)