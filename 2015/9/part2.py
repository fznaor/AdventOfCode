from itertools import permutations 
import math
file1 = open('input.txt', 'r')
lines = file1.readlines()

allCities = []
distances = dict()
for line in lines:
    line = line.strip().split(' ')
    cities = (line[0], line[2])
    for city in cities:
        if not city in allCities:
            allCities.append(city)
    dist = int(line[4])
    distances[tuple(sorted(cities))] = dist
    
maxDist = 0
for a,i in enumerate(list(permutations(allCities))):
    dist = 0
    for j in range(1,len(i)):
        dist += distances[tuple(sorted((i[j-1], i[j])))]
    if dist > maxDist:
        maxDist = dist
print(maxDist)