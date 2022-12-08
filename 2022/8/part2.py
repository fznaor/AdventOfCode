file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = []
for line in [line.strip() for line in lines]:
    row = [int(a) for a in line]
    arr.append(row)
    
rows = len(arr)
cols = len(arr[0])
scores = []

for i in range(1,rows-1):
    for j in range(1,cols-1):
        [u,l,d,r] = [0]*4
        for uu in range(i-1,-1,-1):
            u += 1
            if not arr[i][j] > arr[uu][j]:
                break
        for dd in range(i+1,rows):
            d += 1
            if not arr[i][j] > arr[dd][j]:
                break
        for ll in range(j-1,-1,-1):
            l += 1
            if not arr[i][j] > arr[i][ll]:
                break
        for rr in range(j+1,cols):
            r += 1
            if not arr[i][j] > arr[i][rr]:
                break
        scores.append(u*l*d*r)
print(max(scores))