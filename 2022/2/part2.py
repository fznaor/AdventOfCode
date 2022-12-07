file1 = open('input.txt', 'r')
lines = file1.readlines()

score = 0
for line in lines:
    [op, pl] = line.strip().split(' ')
    
    if op == 'A':
        if pl == 'Z':
            score += 8
        elif pl == 'Y':
            score += 4
        else:
            score += 3
    
    elif op == 'B':
        if pl == 'Z':
            score += 9
        elif pl == 'Y':
            score += 5
        else:
            score += 1
    
    elif op == 'C':
        if pl == 'Z':
            score += 7
        elif pl == 'Y':
            score += 6
        else:
            score += 2
print(score)