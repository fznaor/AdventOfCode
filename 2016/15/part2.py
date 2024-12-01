file1 = open('input.txt', 'r')
lines = file1.readlines()

positionCounts = []
startingPositions = []

for line in [line.strip() for line in lines]:
    positionCounts.append(int(line.split('has ')[1].split()[0]))
    startingPositions.append(int(line.split('position ')[1][:-1]))

positionCounts.append(11)
startingPositions.append(0)

goal = []
for i,(pc,sp) in enumerate(zip(positionCounts,startingPositions)):
    goal.append(pc - 1 - (i % pc))

time = 1
while True:
    for i in range(len(startingPositions)):
        startingPositions[i] += 1
        if startingPositions[i] >= positionCounts[i]:
            startingPositions[i] = 0
    if startingPositions == goal:
        print(time)
        break
    time += 1