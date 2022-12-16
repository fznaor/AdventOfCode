file1 = open('input.txt', 'r')
lines = file1.readlines()

flows = dict()
pipes = dict()
valvesToOpen = []
for line in [line.strip() for line in lines]:
    flows[line.split(' ')[1]] = int(line.split(' ')[4].split('=')[1][:-1])
    if flows[line.split(' ')[1]] > 0:
        valvesToOpen.append(line.split(' ')[1])
    line = line.replace('valve ','valves ')
    pipes[line.split(' ')[1]] = line.split('valves ')[1].split(', ')
    
distances = dict()

for valve in ['AA'] + valvesToOpen:
    visited = []
    queue = []
    queue.append(valve)
    visited.append(valve)
    steps = 1
    while len(queue) > 0:
        newQ = []
        for q in queue:
            for i in pipes[q]:
                if not i in visited:
                    newQ.append(i)
                    visited.append(i)
                    if i in valvesToOpen:
                        distances[(valve,i)] = steps
        queue = newQ
        steps += 1
        
maxFlow = 0
def step(valve,time,toOpen,flow):
    global maxFlow
    if valve != 'AA':
        time -= 1
        flow += time * flows[valve]
        if flow > maxFlow:
            maxFlow = flow
        toOpen.remove(valve)
    if time == 0 or len(toOpen) == 0:
        return
    for v in toOpen:
        if distances[(valve,v)] < time:
            step(v,time-distances[(valve,v)],toOpen.copy(),flow)
            
step('AA',30,valvesToOpen,0)
print(maxFlow)