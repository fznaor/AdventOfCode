file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []

for i,line in enumerate([int(line.strip()) for line in lines]):
    arr.append([line*811589153,i])
    
for rep in range(10):
    ind = 0
    for x in range(len(arr)):
        for i in range(len(arr)):
            if arr[i][1] == x:
                ind = i
                break
        newInd = (ind + arr[ind][0])
        if newInd > len(arr):
            newInd = ind + ((newInd-ind) % (len(arr)-1))
            if newInd >= len(arr):
                newInd %= (len(arr)-1)
        elif newInd < 0:
            newInd = ind + ((newInd-ind) % (len(arr)-1))
            if newInd >= len(arr):
                newInd %= (len(arr)-1)
        if ind > newInd:
            arr.insert(newInd,arr.pop(ind))
        elif ind <= newInd:
            arr.insert(newInd+1,arr[ind])
            del arr[ind]     
        
zind = -1
for i in range(len(arr)):
    if arr[i][0] == 0:
        zind = i
        break
s = 0
for i in range(1000,3001,1000):
    s += arr[(zind+i)%len(arr)][0]
print(s)