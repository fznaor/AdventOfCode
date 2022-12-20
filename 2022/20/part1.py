file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []

for line in [int(line.strip()) for line in lines]:
    arr.append([line, False])
    
ind = 0
for x in range(len(arr)):
    for i in range(len(arr)):
        if not arr[i][1]:
            ind = i
            arr[i][1] = True
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
    
zind = arr.index([0,True])
s = 0
for i in range(1000,3001,1000):
    s += arr[(zind+i)%len(arr)][0]
print(s)