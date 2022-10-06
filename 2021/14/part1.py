import collections

file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = [a for a in lines[0].rstrip()]
rules = []

for i in range(2,len(lines)):
    left = lines[i].rstrip().split(' -> ')[0]
    right = lines[i].rstrip().split(' -> ')[1]
    rules.append([left[0], left[1], right])
    

for step in range(10):
    for i in range(len(arr)-2,-1,-1):
        for rule in rules:
            if arr[i] == rule[0] and arr[i+1] == rule[1]:
                arr.insert(i+1, rule[2])
                break
            
counter = collections.Counter(arr)
most = counter.most_common(1)[-1][1]
least = counter.most_common(len(counter))[-1][1]
print(most-least)