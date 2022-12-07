file1 = open('input.txt', 'r')
lines = file1.readlines()

code = 0
newCode = 0
for line in lines:
    line = line.strip()
    code += len(line)
    newCode += len(line) + line.count('\\') + line.count('"') + 2
print(newCode - code)