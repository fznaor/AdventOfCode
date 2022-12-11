file1 = open('input.txt', 'r')
lines = file1.readlines()

val = 5
for line in [line.strip() for line in lines]:
    for i,c in enumerate(line):
        if c == 'U' and val >= 4:
            val -= 3
        elif c == 'D' and val <= 6:
            val += 3
        elif c == 'L' and val % 3 != 1:
            val -= 1
        elif c == 'R' and val % 3 != 0:
            val += 1
        if i == len(line)-1:
            print(val, end ="")