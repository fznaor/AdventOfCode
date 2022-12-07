file1 = open('input.txt', 'r')
lines = file1.readlines()

code = 0
chars = 0
for line in lines:
    line = line.strip()[1:-1]
    code += len(line) + 2
    skip = 0
    for i,x in enumerate(line):
        if skip > 0:
            skip -= 1
            continue
        if x == "\\":
            chars += 1
            if line[i+1] == '\\' or line[i+1] == '"':
                skip = 1
            elif line[i+1] == 'x':
                skip = 3
        else:
            chars += 1
print(code - chars)