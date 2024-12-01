file1 = open('input.txt', 'r')
lines = file1.readlines()

def toNum(val):
    if val.isdigit():
        return int(val)
    if val == "one":
        return 1
    if val == "two":
        return 2
    if val == "three":
        return 3
    if val == "four":
        return 4
    if val == "five":
        return 5
    if val == "six":
        return 6
    if val == "seven":
        return 7
    if val == "eight":
        return 8
    if val == "nine":
        return 9

valid = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]
s = 0
for line in lines:
    mini = len(line)
    maxi = -1
    minItem = 0
    maxItem = 0
    for item in valid:
        x = line.find(item)
        y = line.rfind(item)
        if x != -1:
            if x < mini:
                mini = x
                minItem = item
            if y >= maxi:
                maxi = y
                maxItem = item
    s += 10 * toNum(minItem) + toNum(maxItem)
print(s)