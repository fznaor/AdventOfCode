file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
for line in [line.strip() for line in lines]:
    game = int(line.split(':')[0].split(' ')[1])
    
    maxColorVals = dict()
    maxColorVals['red'] = 0
    maxColorVals['green'] = 0
    maxColorVals['blue'] = 0
    
    for draw in [draw.strip() for draw in line.split(':')[1].split(';')]:
        for colorVal in draw.split(', '):
            
            color = colorVal.split(' ')[1]
            val = int(colorVal.split(' ')[0])
            
            if val > maxColorVals[color]:
                maxColorVals[color] = val
    
    s += maxColorVals['blue'] * maxColorVals['red'] * maxColorVals['green']
print(s)