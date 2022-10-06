import numpy as np

file1 = open('v21.txt', 'r')
lines = file1.readlines()

res = 0

for line in lines:
    segments = ['', '', '', '', '', '', '', ]
    one = four = seven = eight = ''
    used = ''
    inputs = line.split('|')[0].strip().split(' ')
    for o in inputs:
        if len(o) == 2:
            one = o
            segments[1] = o
            segments[2] = o
            used += o
        elif len(o) == 3:
            seven = o
        elif len(o) == 4:
            four = o
        elif len(o) == 7:
            eight = o
    for digit in seven:
        if digit not in one:
            segments[0] = digit
            used += digit
    for digit in four:
        if digit not in one:
            segments[5] += digit
            segments[6] += digit
            used += digit
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if i not in used:
            segments[3] += i
            segments[4] += i
    multiples = []
    for o in inputs:
        if o not in [one, four, seven, eight]:
            multiples.append(o)
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        count = 0
        for m in multiples:
            for letter in m:
                if letter == i:
                    count += 1
        if count == 3:
            segments[4] = i
            segments[3] = segments[3].replace(i, '')
    discovered = [segments[0], segments[3], segments[4]]
    for m in multiples:
        count = 0
        letters = []
        for letter in m:
            if letter not in discovered:
                count += 1
                letters.append(letter)
        if count == 2:
            for letter in letters:
                if letter in one:
                    segments[1] = letter
                else:
                    segments[6] = letter
        for letter in segments[5]:
            if letter == segments[6]:
                segments[5] = segments[5].replace(letter, '')
        for letter in segments[2]:
            if letter == segments[1]:
                segments[2] = segments[2].replace(letter, '')
    outputs = line.split('|')[1].strip().split(' ')
    power = 3
    for output in outputs:
        indices = []
        for letter in output:
            for i in range(7):
                if letter == segments[i]:
                    indices.append(i)
        indices.sort()
        if indices == [0, 1, 2, 3, 4, 5]:
            res += 0 * pow(10, power)
        elif indices == [1, 2]:
            res += 1 * pow(10, power)
        elif indices == [0, 1, 3, 4, 6]:
            res += 2 * pow(10, power)
        elif indices == [0, 1, 2, 3, 6]:
            res += 3 * pow(10, power)
        elif indices == [1, 2, 5, 6]:
            res += 4 * pow(10, power)
        elif indices == [0, 2, 3, 5, 6]:
            res += 5 * pow(10, power)
        elif indices == [0, 2, 3, 4, 5, 6]:
            res += 6 * pow(10, power)
        elif indices == [0, 1, 2]:
            res += 7 * pow(10, power)
        elif indices == [0, 1, 2, 3, 4, 5, 6]:
            res += 8 * pow(10, power)
        elif indices == [0, 1, 2, 3, 5, 6]:
            res += 9 * pow(10, power)
        power -= 1
print(res)
