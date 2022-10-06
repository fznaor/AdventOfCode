file1 = open('input.txt', 'r')
lines = file1.readlines()

vals = [0]

for line in lines:
    vals.append(int(line.rstrip()))
    
vals.sort()
vals.append(vals[-1]+3)

oneDiff = 0
threeDiff = 0

for i in range(len(vals)-1):
    if vals[i+1] - vals[i] == 1:
        oneDiff += 1
    elif vals[i+1] - vals[i] == 3:
        threeDiff += 1
        
print(oneDiff * threeDiff)