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

for a in allergens:
    for d in dontContain:
        if d in allergens[a]:
             allergens[a][:] = (value for value in allergens[a] if value != d)

for a in allergens:
    maxCount = 1
    toRemove = set()
    for x in allergens[a]:
        if allergens[a].count(x) > maxCount:
            maxCount = allergens[a].count(x)
    for x in allergens[a]:
        if allergens[a].count(x) != maxCount:
             toRemove.add(x)
    for x in toRemove:
        allergens[a][:] = (value for value in allergens[a] if value != x)
    allergens[a] = set(allergens[a])

while True:
    flag = True
    for a in allergens:
        if len(allergens[a]) > 1:
            flag = False
        else:
            for b in allergens:
                if len(allergens[b]) > 1 and list(allergens[a])[0] in allergens[b]:
                    allergens[b].remove(list(allergens[a])[0])
    if flag:
        break
    
res = ""
for a in sorted(allergens):
    res += list(allergens[a])[0] + ","
res = res[:-1]
print(res)