file1 = open('input.txt', 'r')
lines = file1.readlines()

s = 0
for line in lines:
    for item in line.strip():
        if item.isdigit():
            s += 10* int(item)
            break
    for item in line[::-1]:
        if item.isdigit():
            s += int(item)
            break
print(s)