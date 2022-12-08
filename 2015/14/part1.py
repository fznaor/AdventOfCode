file1 = open('input.txt', 'r')
lines = file1.readlines()

reindeer = dict()
for line in [line.strip().split(' ') for line in lines]:
    reindeer[line[0]] = dict()
    reindeer[line[0]]['speed'] = int(line[3])
    reindeer[line[0]]['runtime'] = int(line[6])
    reindeer[line[0]]['rest'] = int(line[13])
    
elapsed = 2503
dists = []
for r in reindeer.values():
    dist = 0
    dist += r['speed']*r['runtime']*(elapsed // (r['runtime']+r['rest']))
    remainingTime = elapsed % (r['runtime']+r['rest']) 
    if remainingTime <= r['runtime']:
        dist += r['speed'] * remainingTime
    else:
        dist += r['speed'] * r['runtime']
    dists.append(dist)
print(max(dists))