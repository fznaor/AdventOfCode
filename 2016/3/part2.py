file1 = open('input.txt', 'r')
lines = file1.readlines()

valid = 0
for i,line in enumerate([" ".join(line.split()) for line in lines]):
    [a,b,c] = [int(x) for x in line.split(' ')]
    if i % 3 == 0:
        t1 = [a]
        t2 = [b]
        t3 = [c]
    else:
        t1.append(a)
        t2.append(b)
        t3.append(c)
    
    if i % 3 == 2:
        for [a,b,c] in [t1,t2,t3]:
            if a+b>c and b+c>a and c+a>b:
                valid += 1
print(valid)