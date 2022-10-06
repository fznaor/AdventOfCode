file1 = open('input.txt', 'r')
lines = file1.readlines()

nums = []

for line in lines:
    nums.append(int(line.rstrip()))
    
for i in range(25, len(nums)):
    sumExists = False
    for j in range(i-25, i):
        for k in range(i-25, i):
            if(j != k and nums[j] != nums[k] and nums[j]+nums[k]==nums[i]):
                sumExists = True
    if not sumExists:
        print(nums[i])
        break