import itertools
import math

playerHit = 100
enemyHit = 100
enemyDamage = 8
enemyArmor = 2

weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armors = [[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

def doesPlayerWin(stats):
    global enemyHit,enemyDamage,enemyArmor
    if stats[1]-enemyArmor > 0:
        playerMovesToWin = math.ceil(enemyHit/(stats[1]-enemyArmor))
    else:
        playerMovesToWin = enemyHit
    if enemyDamage-stats[2] > 0:
        enemyMovesToWin = math.ceil(playerHit/(enemyDamage-stats[2]))
    else:
        enemyMovesToWin = playerHit
    return playerMovesToWin <= enemyMovesToWin

allCombs = []
for weapon in weapons:
    for armor in armors:
        # without armor
        allCombs.append(weapon)
        for ring in rings:
            allCombs.append([sum(x) for x in zip(weapon,ring)])
        for ringPair in itertools.combinations(rings,2):
            allCombs.append([sum(x) for x in zip(weapon,ringPair[0],ringPair[1])])
        # with armor
        allCombs.append([sum(x) for x in zip(weapon,armor)])
        for ring in rings:
            allCombs.append([sum(x) for x in zip(weapon,armor,ring)])
        for ringPair in itertools.combinations(rings,2):
            allCombs.append([sum(x) for x in zip(weapon,armor,ringPair[0],ringPair[1])])
                 
allCombs = sorted(allCombs, key=lambda x: x[0])
for comb in allCombs:
    if doesPlayerWin(comb):
        print(comb[0])
        break
