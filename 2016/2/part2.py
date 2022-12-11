file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = [['x','x','1','x','x'],
       ['x','2','3','4','x'],
       ['5','6','7','8','9'],
       ['x','A','B','C','x'],
       ['x','x','D','x','x']]
ii = 2
jj = 0
for line in [line.strip() for line in lines]:
    for i,c in enumerate(line):
        if c == 'U' and ii > 0:
            if arr[ii-1][jj] != 'x':
                ii -= 1
        elif c == 'D' and ii < len(arr)-1:
            if arr[ii+1][jj] != 'x':
                ii += 1
        elif c == 'L' and jj > 0:
            if arr[ii][jj-1] != 'x':
                jj -= 1
        elif c == 'R' and jj < len(arr)-1:
            if arr[ii][jj+1] != 'x':
                jj += 1
        if i == len(line)-1:
            print(arr[ii][jj], end ="")