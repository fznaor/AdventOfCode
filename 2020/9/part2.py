file1 = open('input.txt', 'r')
lines = file1.readlines()

nums = []
target = 393911906
found = False

for line in lines:
    nums.append(int(line.rstrip()))
    
for i in range(len(nums)):
    suma = nums[i]
    for j in range(i+1, len(nums)):
        suma += nums[j]
        if suma > target:
            break
        elif suma == target:
            print(max(nums[i:j+1]) + min(nums[i:j+1]))
            found = True
    if found:
        break