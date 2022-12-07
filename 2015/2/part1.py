file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
for line in lines:
    [l,w,h] = [int(x) for x in line.strip().split('x')]
    res += 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])
print(res)