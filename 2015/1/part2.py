file1 = open('input.txt', 'r')
lines = file1.readlines()

floor = 0
for i,c in enumerate(lines[0].strip()):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        print(i+1)
        break