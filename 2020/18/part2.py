from functools import reduce

file1 = open('input.txt', 'r')
lines = file1.readlines()

def calc(line, index):
    nums = []
    op = None
    
    while True:
        if line[index] == '+':
            op = 'sum'
        elif line[index] == '*':
            op = 'mul'
        elif line[index] == '(':
            res, idx = calc(line, index+1)
            nums.append(res)
            index = idx
            if op == 'sum':
                nums[-2] = nums[-2] + nums[-1]
                del nums[-1]
        elif line[index] == ')':
            return reduce((lambda x, y: x * y), nums), index
        else:
            nums.append(int(line[index]))
            if op == 'sum':
                nums[-2] = nums[-2] + nums[-1]
                del nums[-1]
        index += 1
suma = 0

for line in lines:
    line = line.rstrip()
    line = line.replace(" ","")
    line = '(' + line + ')'
    suma += calc(line,1)[0]

print(suma)