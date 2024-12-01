file1 = open('input.txt', 'r')
lines = file1.readlines()

def getNum(arr, row, col):
    start = col
    end = col
    
    while start >= 0:
        start -= 1
        if not arr[row][start].isdigit():
            start += 1
            break
    while end < dim:
        end += 1
        if not arr[row][end].isdigit():
            end -= 1
            break
    return int(arr[row][start:end+1]), end

def sumOfTwoAdjNumbers(arr, row, col):
    nums = []
    for i in range(row-1, row+2):
        j = col - 1
        while j <= col + 1:
            if i < 0 or i >= dim or j < 0 or j >= dim:
                continue
            if arr[i][j].isdigit():
                num, end = getNum(arr, i, j)
                j = end + 1
                nums.append(num)
            else:
                j += 1
    if len(nums) == 2:
        return nums[0] * nums[1]
    else:
        return 0

dim = len(lines)
s = 0
for i,line in enumerate([line.strip() for line in lines]):
    for j,val in enumerate(line):
        if val == '*':
            s += sumOfTwoAdjNumbers(lines,i,j)
print(s)