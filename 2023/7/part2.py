import collections
import functools

ranks = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 1,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
}

def getStrength(cards):
    freqs = collections.Counter(cards)
    jCount = 0
    if 'J' in freqs:
        jCount = freqs['J']
    del freqs['J']
    freqs = [x for x in freqs.values()]
    freqs.sort(reverse = True)
    if len(freqs) == 0:
        freqs = [5]
    else:
        freqs[0] += jCount
    if freqs[0] == 5:
        return 7
    if freqs[0] == 4:
        return 6
    if freqs[0] == 3 and freqs[1] == 2:
        return 5
    if freqs[0] == 3:
        return 4
    if freqs[0] == 2 and freqs[1] == 2:
        return 3
    if freqs[0] == 2:
        return 2
    return 1

def compare(x,y):
    if x[2] == y[2]:
        for valX,valY in zip(x[0],y[0]):
            if ranks[valX] == ranks[valY]:
                continue
            if ranks[valX] > ranks[valY]:
                return 1
            else:
                return -1
    if x[2] > y[2]:
        return 1
    else: 
        return -1

file1 = open('input.txt', 'r')
lines = file1.readlines()
hands = []

for line in [line.strip() for line in lines]:
    cards = [x for x in line.split()[0]]
    val = int(line.split()[1])
    hands.append([cards,val,getStrength(cards)])

sortedHands = sorted(hands, key=functools.cmp_to_key(compare), reverse = True)

s = 0
for i,hand in enumerate(sortedHands[-1::-1]):
    s += (i+1) * hand[1]
print(s)