inp = "156794823"
nums = [int(i) for i in inp] + [n for n in range(10,1000001)]

vals = dict()
for i,num in enumerate(nums):
    if i+1 < len(nums):
        vals[num] = nums[i+1]
    else:
        vals[num] = nums[0]
   
pivot = nums[0]     
for it in range(10000000):
    first = vals[pivot]
    second = vals[first]
    third = vals[second]
    dest = pivot - 1 if pivot != 1 else 1000000
    while dest in [first,second,third]:
        dest -= 1
        if dest == 0:
            dest = 1000000
    vals[pivot] = vals[third]
    vals[third] = vals[dest]
    vals[dest] = first
    pivot = vals[pivot]
print(vals[1]*vals[vals[1]])