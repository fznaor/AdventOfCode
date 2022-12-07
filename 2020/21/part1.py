file1 = open('input.txt', 'r')
lines = file1.readlines()

allergens = dict()
allIngredients = set()
canContain = set()
ingrCount = dict()

for line in lines:
    line = line.strip()
    lineParts = line.split('(')
    ing = lineParts[0].split(' ')[:-1]
    for i in ing:
        if not i in ingrCount:
            ingrCount[i] = 1
        else:
            ingrCount[i] += 1
    al = lineParts[1].split('contains ')[1].split(', ')
    al[-1] = al[-1][:-1]
    for allergen in al:
        if not allergen in allergens:
            allergens[allergen] = ing.copy()
        else:
            allergens[allergen].extend(ing.copy())
    allIngredients.update(ing)
    
    
for a in allergens:
    maxCount = 1
    for x in allergens[a]:
        if allergens[a].count(x) > maxCount:
            maxCount = allergens[a].count(x)
    for x in allergens[a]:
        if allergens[a].count(x) == maxCount:
            canContain.add(x)

dontContain = allIngredients.copy()
for x in canContain:
    dontContain.remove(x)

count = 0
for x in dontContain:
    count += ingrCount[x]
print(count)