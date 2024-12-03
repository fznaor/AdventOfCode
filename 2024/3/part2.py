import re

file1 = open('input.txt', 'r')
lines = file1.readlines()

res = 0
regex = ''
for line in lines:
    regex += line.strip()

match = re.findall('don\'t.*?(?:do[^n]|$)', regex)
for m in match:
    regex = regex.replace(m, '')

match = re.findall('mul\((\d{1,3}),(\d{1,3})\)', regex)
for a,b in match:
    res += int(a) * int(b)

print(res)