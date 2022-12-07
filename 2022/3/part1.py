file1 = open('input.txt', 'r')
lines = file1.readlines()

score = 0
for line in lines:
    line = line.strip()
    firstHalf = set()
    for i,c in enumerate(line):
        if i < len(line)/2:
            firstHalf.add(c)
        else:
            if c in firstHalf:
                if c >= 'a' and c <= 'z':
                    score += ord(c) - 96
                else:
                    score += ord(c) - 38
                break
print(score)