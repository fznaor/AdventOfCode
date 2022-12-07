file1 = open('input.txt', 'r')
lines = file1.readlines()

def mapMove(move):
    if move == 'X':
        return 'A'
    elif move == 'Y':
        return 'B'
    else:
        return 'C'

score = 0
for line in lines:
    [op, pl] = line.strip().split(' ')
    pl = mapMove(pl)
    
    if pl == 'A':
        score += 1
    elif pl == 'B':
        score += 2
    else:
        score += 3
    
    if op == pl:
        score += 3
        
    if (pl == 'A' and op == 'C') or (pl == 'B' and op == 'A') or (pl == 'C' and op == 'B'):
        score += 6
print(score)