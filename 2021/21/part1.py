p1 = 5
p2 = 8
p1Score = 0
p2Score = 0
p1Wins = 0
p2Wins = 0

#111 *1 3
#222 *1 6
#333 *1 9
#122 *3 5
#133 *3 7
#211 *3 4
#233 *3 8
#311 *3 5
#322 *3 7
#123 *6 6

def turn(p1, p2, p1Score, p2Score, toAdd, whoseTurn, realityCount):
    global p1Wins, p2Wins
    if whoseTurn == 1:
        p1 += toAdd
        p1 %= 10
        if p1 == 0:
            p1 = 10
        p1Score += p1
        if p1Score >= 21:
            p1Wins += realityCount
            return
    else:
        p2 += toAdd
        p2 %= 10
        if p2 == 0:
            p2 = 10
        p2Score += p2
        if p2Score >= 21:
            p2Wins += realityCount
            return
        
    if whoseTurn == 1:
        toPlay = 0
    else:
        toPlay = 1
    
    turn(p1, p2, p1Score, p2Score, 3, toPlay, realityCount * 1)
    turn(p1, p2, p1Score, p2Score, 4, toPlay, realityCount * 3)
    turn(p1, p2, p1Score, p2Score, 5, toPlay, realityCount * 6)
    turn(p1, p2, p1Score, p2Score, 6, toPlay, realityCount * 7)
    turn(p1, p2, p1Score, p2Score, 7, toPlay, realityCount * 6)
    turn(p1, p2, p1Score, p2Score, 8, toPlay, realityCount * 3)
    turn(p1, p2, p1Score, p2Score, 9, toPlay, realityCount * 1)
    

toPlay = 1    
realityCount = 1
turn(p1, p2, p1Score, p2Score, 3, toPlay, realityCount * 1)
turn(p1, p2, p1Score, p2Score, 4, toPlay, realityCount * 3)
turn(p1, p2, p1Score, p2Score, 5, toPlay, realityCount * 6)
turn(p1, p2, p1Score, p2Score, 6, toPlay, realityCount * 7)
turn(p1, p2, p1Score, p2Score, 7, toPlay, realityCount * 6)
turn(p1, p2, p1Score, p2Score, 8, toPlay, realityCount * 3)
turn(p1, p2, p1Score, p2Score, 9, toPlay, realityCount * 1)
print(max([p1Wins, p2Wins]))