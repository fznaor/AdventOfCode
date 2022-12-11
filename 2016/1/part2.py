file1 = open('input.txt', 'r')
lines = file1.readlines()

i = 0
j = 0
drctn = 0 #nesw
vals = lines[0].strip().split(', ')
visited = []
for val in vals:
    [si, sj] = [i, j]
    [d,n] = [val[0], int(val[1:])]
    if d == 'R':
        drctn += 1
    else:
        drctn -= 1
    drctn %= 4
    found = False
    if drctn == 0:
        i -= n
        for ii in range(si-1,i-1,-1):
            if (ii,j) in visited:
                print(abs(ii)+abs(j))
                found = True
                break
            visited.append((ii,j))
    elif drctn == 1:
        j += n
        for jj in range(sj+1,j+1):
            if (i,jj) in visited:
                print(abs(i)+abs(jj))
                found = True
                break
            visited.append((i,jj))
    elif drctn == 2:
        i += n
        for ii in range(si+1,i+1):
            if (ii,j) in visited:
                print(abs(ii)+abs(j))
                found = True
                break
            visited.append((ii,j))
    else:
        j -= n
        for jj in range(sj-1,j-1,-1):
            if (i,jj) in visited:
                print(abs(i)+abs(jj))
                found = True
                break
            visited.append((i,jj))
    if found:
        break