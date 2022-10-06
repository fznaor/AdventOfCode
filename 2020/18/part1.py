file1 = open('input.txt', 'r')
lines = file1.readlines()

def calc(line, index):
    current = 0
    op = None
    
    while True:
        if line[index] == '+':
            op = 'sum'
        elif line[index] == '*':
            op = 'mul'
        elif line[index] == '(':
            if op == 'sum':
                res, idx = calc(line, index+1)
                current += res
                index = idx
            elif op == 'mul':
                res, idx = calc(line, index+1)
                current *= res
                index = idx
            else:
                res, idx = calc(line, index+1)
                current = res
                index = idx
        elif line[index] == ')':
            return current, index
        elif current == 0:
            current = int(line[index])
        else:
            if op == 'sum':
                current += int(line[index])
            else:
                current *= int(line[index])
        index += 1
        
suma = 0

for line in lines:
    line = line.rstrip()
    line = line.replace(" ","")
    line = '(' + line + ')'
    suma += calc(line,1)[0]

print(suma)