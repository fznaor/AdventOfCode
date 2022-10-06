start = [12,1,16,3,11,0]
nums = {}
turn = 0
nextVal = None

for num in start:
    turn += 1
    nums[num] = turn
    nextVal = 0
    
while turn != (30000000-1):
    turn += 1
    if not nextVal in nums:
        nums[nextVal] = turn
        nextVal = 0
    else:
        t = nums[nextVal]
        nums[nextVal] = turn
        nextVal = turn - t
print(nextVal)