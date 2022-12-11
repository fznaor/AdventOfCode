file1 = open('input.txt', 'r')
lines = file1.readlines()

valid = 0
for line in [" ".join(line.split()) for line in lines]:
    [a,b,c] = [int(x) for x in line.split(' ')]
    if a+b>c and b+c>a and c+a>b:
        valid += 1
print(valid)