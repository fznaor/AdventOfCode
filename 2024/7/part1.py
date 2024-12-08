file1 = open('input.txt', 'r')
lines = file1.readlines()

def isValid(target, nums, currentPos, currentSum):
    if currentSum > target:
        return

    if currentPos == len(nums) - 1:
        if currentSum == target:
            validTargets.add(target)
        return
    isValid(target, nums, currentPos + 1, currentSum + nums[currentPos+1])
    isValid(target, nums, currentPos + 1, currentSum * nums[currentPos+1])

vals = dict()
validTargets = set()

for line in [line.strip() for line in lines]:
    target, nums = line.split(': ')
    target = int(target)
    nums = [int(x) for x in nums.split(' ')]
    vals[target] = nums
    isValid(target, nums, 0, nums[0])

print(sum(validTargets))