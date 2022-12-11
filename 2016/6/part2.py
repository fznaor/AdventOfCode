file1 = open('input.txt', 'r')
lines = file1.readlines()

vals = []
for line in [line.strip() for line in lines]:
    vals.append([l for l in line])
    
for j in range(len(vals[0])):
    print(min([i[j] for i in vals], key=[i[j] for i in vals].count), end='')