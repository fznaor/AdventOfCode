file1 = open('input.txt', 'r')
lines = file1.readlines()

vals = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for line in lines:
    line = line.strip().split(' ')
    index = int(line[1][:-1])
    d1 = line[2][:-1]
    v1 = int(line[3][:-1])
    d2 = line[4][:-1]
    v2 = int(line[5][:-1])
    d3 = line[6][:-1]
    v3 = int(line[7])
    found = True
    for d,v in zip([d1,d2,d3],[v1,v2,v3]):
        if d in ['cats','trees']:
            if not v > vals[d]:
               found = False
               break 
        elif d in ['pomeranians','goldfish']:
            if not v < vals[d]:
               found = False
               break 
        elif not vals[d] == v:
            found = False
            break
    if found:
        print(index)
        break