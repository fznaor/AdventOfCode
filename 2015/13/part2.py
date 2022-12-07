from itertools import permutations
file1 = open('input.txt', 'r')
lines = file1.readlines()

people = ['Me']
rels = dict()
for line in lines:
    line = line.strip().split()
    a = line[0]
    b = line[10][:-1]
    if not a in people:
        people.append(a)
    if not b in people:
        people.append(b)
    if line[2] == 'gain':
        num = int(line[3])
    else:
        num = -1*int(line[3])
    rels[(a,b)] = num
    
for person in people:
    rels[(person,'Me')] = 0
    rels[('Me',person)] = 0
    
arrs = permutations(people[1:])
scores = []
for arr in arrs:
    score = 0
    for i,person in enumerate(arr):
        if i==0:
            score += rels[(person,people[0])] + rels[(people[0],person)]
            score += rels[(person,arr[i+1])]
        elif i==len(arr)-1:
            score += rels[(person,people[0])] + rels[(people[0],person)]
            score += rels[(person,arr[i-1])]
        else:
            score += rels[(person,arr[i-1])]
            score += rels[(person,arr[i+1])]
    scores.append(score)
print(max(scores))