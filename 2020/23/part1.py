inp = "156794823"
nums = [int(i) for i in inp]

for it in range(100):
    toMove = nums[1:4]
    nums = nums[0:1] + nums[4:]
    pivot = nums[0] - 1 if nums[0] != 1 else 9
    while pivot in toMove:
        pivot -= 1
        if pivot == 0:
            pivot = 9
    toMove = [pivot] + toMove
    for i,el in enumerate(nums):
        if el == pivot:
            nums[i:i+1] = toMove 
            break
    nums = nums[1:9] + nums[0:1]
print(nums)