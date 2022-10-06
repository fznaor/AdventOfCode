file1 = open('v20.txt', 'r')
Lines = file1.readlines()

bags = {}
 
for line in Lines:
    line = line.rstrip()
    line = line.split('contain ')
    bagName = line[0].split(' bags')[0]
    children = line[1].split(', ')
    for child in children:
        xxx = child.split(' ', 1)
        num = xxx[0]
        bag = xxx[1].split(' bag')[0]
        if bag == 'other':
            bags[bagName] = {}
            continue
        if bagName in bags.keys():
            bags[bagName][bag] =num
        else:
            bags[bagName] = {bag:num}
        
#print(bags)

count = 0

def preorder(key, value):
    suma = value
    for b in bags[key]:
        suma += preorder(b,value * int(bags[key][b]))
    return suma

count = preorder("shiny gold", 1)

print(count-1)