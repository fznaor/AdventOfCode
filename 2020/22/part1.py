file1 = open('input.txt', 'r')
lines = file1.readlines()

p1 = lines[1:26]
p2 = lines[28:53]

for i in range(25):
    p1[i] = int(p1[i].rstrip())
    p2[i] = int(p2[i].rstrip())
    
while True:
    a = p1.pop(0)
    b = p2.pop(0)
   
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)
    if len(p1) == 0:
        winner = p2
        break
    elif len(p2) == 0:
        winner = p1
        break
    
score = 0
for i,val in enumerate(winner):
    score += (len(winner)-i)*val
print(score)