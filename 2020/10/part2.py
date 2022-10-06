file1 = open('input.txt', 'r')
lines = file1.readlines()

vals = [0]

for line in lines:
    vals.append(int(line.rstrip()))
    
vals.sort()
vals.append(vals[-1]+3)

res = 1
    
def coef(i, chainSize):
    suma = 0
    if i == chainSize:
        return 1
    for j in range(i+1, i+4):
        if j > chainSize:
            break
        suma += coef(j, chainSize)
    return suma

chainSize = 0
for i in range(len(vals)-1):
    if vals[i+1] - vals[i] == 1:
        chainSize += 1
    else:
        chainSize += 1
        if chainSize > 2:
            res *= coef(1, chainSize)
        chainSize = 0

print(res)