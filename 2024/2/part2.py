file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0

def checkList(vals):
    isIncrease = None
    isValid = True
    for i,(a,b) in enumerate(zip(vals[:-1], vals[1:])):
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
    return isValid

res = 0
for line in lines:
    nums = [int(x) for x in line.strip().split()]
    if(checkList(nums)):
        res += 1
    else:
        for i in range(len(nums)):
            if(checkList(nums[:i] + nums[i+1:])):
                res += 1
                break
    
print(res)