import copy

file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = [a for a in lines[0].rstrip()]
rules = {}
counts = {}
freqs = {}

for i in range(2,len(lines)):
    left = lines[i].rstrip().split(' -> ')[0]
    right = lines[i].rstrip().split(' -> ')[1]
    rules[(left[0], left[1])] = right
    counts[(left[0], left[1])] = 0
    
for i in range(len(arr)-1):
    counts[(arr[i], arr[i+1])] += 1

for i in range(len(arr)):
    if arr[i] not in freqs:
        freqs[arr[i]] = 1
    else:
        freqs[arr[i]] += 1
    
for i in range(40):
    newCounts = copy.deepcopy(counts)
    for (a,b) in counts:
        if counts[(a,b)] == 0:
            continue
        else:
            newCounts[(a,rules[(a,b)])] += counts[(a,b)]
            newCounts[(rules[(a,b)],b)] += counts[(a,b)]
            newCounts[(a,b)] -= counts[(a,b)]
            if rules[(a,b)] not in freqs:
                freqs[rules[(a,b)]] = counts[(a,b)]
            else:
                freqs[rules[(a,b)]] += counts[(a,b)]
    counts = newCounts

print(freqs[max(freqs, key=freqs.get)] - freqs[min(freqs, key=freqs.get)])