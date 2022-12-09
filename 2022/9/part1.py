file1 = open('input.txt', 'r')
lines = file1.readlines()

[hx,hy,tx,ty] = [0]*4
tailPositions = []

for line in [line.strip().split(' ') for line in lines]:
    direction = line[0]
    val = int(line[1])
    
    for i in range(val):
        if direction == 'U':
            if hx < tx:
                tx -= 1
                ty = hy
            hx -= 1
            tailPositions.append((tx,ty))
        elif direction == 'D':
            if hx > tx:
                tx += 1
                ty = hy
            hx += 1
            tailPositions.append((tx,ty))
        elif direction == 'L':
            if hy < ty:
                ty -= 1
                tx = hx
            hy -= 1
            tailPositions.append((tx,ty))
        else:
            if hy > ty:
                ty += 1
                tx = hx
            hy += 1
            tailPositions.append((tx,ty))
print(len(set(tailPositions)))