file1 = open('input.txt', 'r')
lines = file1.readlines()

sequence = ""

for line in [line.strip() for line in lines]:
    sequence += line

s = 0
for seg in sequence.split(','):
    x = 0
    for c in seg:
        x += ord(c)
        x *= 17
        x %= 256
    s += x
print(s)