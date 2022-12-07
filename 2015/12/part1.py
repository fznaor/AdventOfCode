import json
file1 = open('input.txt', 'r')
lines = file1.readlines()
line = lines[0].strip()
res = 0

def parse(data,ty):
    global res
    if ty == 'list':
        for x in data:
            parse(x,type(x).__name__)
    elif ty == 'dict':
        for x in data:
            parse(data[x],type(data[x]).__name__)
    elif ty == 'int':
        res += data

y = json.loads(line)
parse(y,'dict')
print(res)