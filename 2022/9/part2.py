file1 = open('input.txt', 'r')
lines = file1.readlines()

def moveTail(hx,hy,tx,ty):
    if hx-tx == 2:
        tx = hx-1
        if hy>ty:
            ty += 1
        elif hy<ty:
            ty -= 1
    elif tx-hx == 2:
        tx  = hx+1
        if hy>ty:
            ty += 1
        elif hy<ty:
            ty -= 1
    elif hy-ty == 2:
        ty = hy-1
        if hx>tx:
            tx += 1
        elif hx<tx:
            tx -= 1
    elif ty-hy == 2:
        ty = hy+1
        if hx>tx:
            tx += 1
        elif hx<tx:
            tx -= 1
    return tx,ty

knots = []
for i in range(10):
    knots.append((0,0))
tailPositions = []

for line in [line.strip().split(' ') for line in lines]:
    direction = line[0]
    val = int(line[1])
    
    for i in range(val):
        for j in range(9):
            if j == 0:
                (a,b) = knots[0]
                if direction == 'U':
                    knots[0] = (a-1,b)
                elif direction == 'D':
                    knots[0] = (a+1,b)
                elif direction == 'L':
                    knots[0] = (a,b-1)
                else:
                    knots[0] = (a,b+1)
            (hx,hy) = knots[j]
            (tx,ty) = knots[j+1]
            tx,ty = moveTail(hx,hy,tx,ty)
            knots[j+1] = (tx,ty)
            if j == 8:
                tailPositions.append(knots[j+1])
        
        
print(len(set(tailPositions)))