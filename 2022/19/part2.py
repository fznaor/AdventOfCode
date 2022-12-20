file1 = open('input.txt', 'r')
lines = file1.readlines()

def step(timeRem, ore, clay, obs, geo, robots, res):
    global maxx, hist
    if tuple([timeRem]+robots+res) in hist:
        return
    else:
        hist.add(tuple([timeRem]+robots+res))
    x = res[-1]
    h = res[-1]
    for i in range(1,timeRem+1):
        h += x + i
    if h <= maxx:
        return
    if timeRem == 0:
        if res[-1] > maxx:
            maxx = res[-1]
            print(maxx)
        return
    count = 0
    if res[0] >= geo[0] and res[2] >= geo[1]:
        count += 1
        newRes = [res[0]-geo[0], res[1], res[2]-geo[1], res[3]]
        newRobots = [robots[0], robots[1], robots[2], robots[3]+1]
        for i in range(4):
            newRes[i] += robots[i]
        step(timeRem - 1, ore, clay, obs, geo, newRobots, newRes)
    else:
        if res[0] >= ore and robots[0] <= max(ore,clay,obs[0],geo[0]) and res[0] <= max(ore,clay,obs[0],geo[0]):
            count += 1
            newRes = [res[0]-ore, res[1], res[2], res[3]]
            newRobots = [robots[0]+1, robots[1], robots[2], robots[3]]
            for i in range(4):
                newRes[i] += robots[i]
            step(timeRem - 1, ore, clay, obs, geo, newRobots, newRes)
        if res[0] >= clay and robots[1] <= obs[1] and res[1] <= obs[1]:
            count += 1
            newRes = [res[0]-clay, res[1], res[2], res[3]]
            newRobots = [robots[0], robots[1]+1, robots[2], robots[3]]
            for i in range(4):
                newRes[i] += robots[i]
            step(timeRem - 1, ore, clay, obs, geo, newRobots, newRes)
        if res[0] >= obs[0] and res[1] >= obs[1] and robots[2] <= geo[1]:
            count += 1
            newRes = [res[0]-obs[0], res[1]-obs[1], res[2], res[3]]
            newRobots = [robots[0], robots[1], robots[2]+1, robots[3]]
            for i in range(4):
                newRes[i] += robots[i]
            step(timeRem - 1, ore, clay, obs, geo, newRobots, newRes)
        
        for i in range(4):
            res[i] += robots[i]
        step(timeRem-1, ore, clay, obs, geo, robots, res)
        
result = 0
for i,line in enumerate([line.strip().split(' ') for line in lines]):
    ore = int(line[6])
    clay = int(line[12])
    obs = [int(line[18]), int(line[21])]
    geo = [int(line[27]), int(line[30])]
    
    robots = [1,0,0,0]
    res = [0,0,0,0]
    maxx = 0
    hist = set()
    step(32,ore,clay,obs,geo,robots,res)
    print(maxx)
    result += (i+1) * maxx
print(result)