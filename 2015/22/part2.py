import math
bossHit = 58
bossDmg = 9
plHit = 50
plArmor = 0
mana = 500
spentMana = 0
shieldCount = -1
poisonCount = -1
rechargeCount = -1
minMana = math.inf

def playMove(bossHit,plHit,plArmor,mana,spentMana,shieldCount,poisonCount,rechargeCount,playerMove):
    global minMana
    shieldCount -= 1
    poisonCount -= 1
    rechargeCount -= 1
    
    plHit -= 1
    if plHit == 0:
        return
    
    if poisonCount >= 0:
        bossHit -= 3
    if rechargeCount >= 0:
        mana += 101
    if shieldCount == 0:
        plArmor -= 7
    if bossHit <= 0:
        if spentMana < minMana:
            minMana = spentMana
        return
    
    if playerMove:
        if mana < 53:
            return
        
        #magic missile
        if mana >= 53:
            newBossHit = bossHit - 4
            if newBossHit <= 0:
                if spentMana + 53 < minMana:
                    minMana = spentMana + 53
                return
            elif not(spentMana + 53 >= minMana):
                playMove(newBossHit,plHit,plArmor,mana-53,spentMana+53,shieldCount,poisonCount,rechargeCount,False)
            
        #drain
        if mana >= 73:
            newBossHit = bossHit - 2
            if newBossHit <= 0:
                if spentMana + 73 < minMana:
                    minMana = spentMana + 73
                return
            elif not(spentMana + 73 >= minMana):
                playMove(newBossHit,plHit+2,plArmor,mana-73,spentMana+73,shieldCount,poisonCount,rechargeCount,False)
            
        #shield
        if mana >= 113 and shieldCount <= 0 and spentMana + 113 < minMana:
            playMove(bossHit,plHit,plArmor+7,mana-113,spentMana+113,6,poisonCount,rechargeCount,False)
            
        #poison
        if mana >= 173 and poisonCount <= 0 and spentMana + 173 < minMana:
            playMove(bossHit,plHit,plArmor,mana-173,spentMana+173,shieldCount,6,rechargeCount,False)
            
        #recharge
        if mana >= 229 and rechargeCount <= 0 and spentMana + 229 < minMana:
            playMove(bossHit,plHit,plArmor,mana-229,spentMana+229,shieldCount,poisonCount,5,False)
    else:
        if plHit - bossDmg + plArmor <= 0:
            return
        playMove(bossHit,plHit-bossDmg+plArmor,plArmor,mana,spentMana,shieldCount,poisonCount,rechargeCount,True)
        
playMove(bossHit,plHit,plArmor,mana,spentMana,shieldCount,poisonCount,rechargeCount,True)
print(minMana)