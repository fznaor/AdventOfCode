file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
target = 150

def checkAllSubsets(v,s,i):
    global res, target
    
    for j in range(i+1,len(v)):
        if s+v[j] < target:
            checkAllSubsets(v,s+v[j],j)
        elif s+v[j] == target:
            res += 1
        else:
            return

vals = []
for line in [line.strip() for line in lines]:
    vals.append(int(line))
vals.sort()

for i in range(len(vals)):
    checkAllSubsets(vals,vals[i],i)
print(res)