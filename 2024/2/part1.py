file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
for line in lines:
    nums = [int(x) for x in line.strip().split()]
    
    isIncrease = None
    isValid = True
    for a,b in zip(nums[:-1], nums[1:]):
        if(a == b):
            isValid = False
            break
        if(isIncrease == None):
            isIncrease = a > b
        if(a > b and not isIncrease or a < b and isIncrease):
            isValid = False
            break
        elif(abs(a-b) > 3):
            isValid = False
            break
    if(isValid):
        res += 1
print(res)