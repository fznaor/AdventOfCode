file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
for line in [line.strip() for line in lines]:
    game = int(line.split(':')[0].split(' ')[1])
    valid = True
    
    for draw in [draw.strip() for draw in line.split(':')[1].split(';')]:
        for colorVal in draw.split(', '):
            
            color = colorVal.split(' ')[1]
            val = int(colorVal.split(' ')[0])
            
            if color == 'red' and val > 12 or color == 'green' and val > 13 or color == 'blue' and val > 14:
                valid = False
                break
        if not valid:
            break
      
    if valid:
        s += game
print(s)