import copy

file1 = open('input.txt', 'r')
lines = file1.readlines()

p1 = lines[1:26]
p2 = lines[28:53]

for i in range(25):
    p1[i] = int(p1[i].rstrip())
    p2[i] = int(p2[i].rstrip())
    
def play(p1,p2):
    configs = []
    while True:
        if [p1,p2] in configs:
            return [1,p1]
        else:
            configs.append([copy.deepcopy(p1),copy.deepcopy(p2)])
            
        a = p1.pop(0)
        b = p2.pop(0)
        
        if a <= len(p1) and b <= len(p2):
            winner, nop = play(p1[:a], p2[:b])
            if winner == 1:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
            if len(p1) == 0:
                return [2,p2]
            elif len(p2) == 0:
                return [1,p1]
        else:
            if a > b:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
            if len(p1) == 0:
                return [2,p2]
            elif len(p2) == 0:
                return [1,p1]

winner, arr = play(p1,p2)
score = 0
for i,val in enumerate(arr):
    score += (len(arr)-i)*val
print(score)