file1 = open('input.txt', 'r')
lines = file1.readlines()

floor = 0
for c in lines[0].strip():
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
print(floor)