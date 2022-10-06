file1 = open('input.txt', 'r')
lines = file1.readlines()

scanners = []
newScanner = []
deducedScanners = [0]
unknownScanners = []
allBeacons = []
scannerLocs = [[0,0,0]]
rotations = [(0,1,2,1,1,1),
             (0,1,2,1,-1,-1),
             (0,1,2,-1,-1,1),
             (0,1,2,-1,1,-1),
             (0,2,1,1,-1,1),
             (0,2,1,1,1,-1),
             (0,2,1,-1,1,1),
             (0,2,1,-1,-1,-1),
             (1,2,0,1,1,1),
             (1,0,2,1,-1,1),
             (1,2,0,1,-1,-1),
             (1,0,2,1,1,-1),
             (1,2,0,-1,-1,1),
             (1,0,2,-1,1,1),
             (1,2,0,-1,1,-1),
             (1,0,2,-1,-1,-1),
             (2,0,1,1,1,1),
             (2,1,0,1,-1,1),
             (2,0,1,1,-1,-1),
             (2,1,0,1,1,-1),
             (2,0,1,-1,-1,1),
             (2,1,0,-1,1,1),
             (2,0,1,-1,1,-1),
             (2,1,0,-1,-1,-1)]

for line in lines:
    if len(line.rstrip()) == 0:
        scanners.append(newScanner)
        newScanner = []
        continue
    
    if 'scanner' in line:
        continue
    else:
        beacons = [int(i) for i in line.rstrip().split(',')]
        newScanner.append(beacons)
scanners.append(newScanner)
unknownScanners.extend(range(1,len(scanners)))
allBeacons.extend(scanners[0])

while len(unknownScanners) != 0:
    for i in deducedScanners:
        for j in unknownScanners:
            for (a,b,c,d,e,f) in rotations:
                distances = []
                for ii,scanI in enumerate(scanners[i]):
                    for jj,scanJ in enumerate(scanners[j]):
                        newScanJ = [d*scanJ[a], e*scanJ[b], f*scanJ[c]]
                        distances.append((newScanJ[2]-scanI[2])**2 + (newScanJ[1]-scanI[1])**2 + (newScanJ[0]-scanI[0])**2)
                mostCommon = max(set(distances), key=distances.count)
                maxFreq = distances.count(mostCommon)
                if maxFreq >= 12:
                    foundOffset = False
                    for ii,scanI in enumerate(scanners[i]):
                        for jj,scanJ in enumerate(scanners[j]):
                            newScanJ = [d*scanJ[a], e*scanJ[b], f*scanJ[c]]
                            distance = (newScanJ[2]-scanI[2])**2 + (newScanJ[1]-scanI[1])**2 + (newScanJ[0]-scanI[0])**2
                            if distance == mostCommon:
                                offset = [scanI[0] - newScanJ[0], scanI[1] - newScanJ[1], scanI[2] - newScanJ[2]]
                                scannerLocs.append(offset)
                                foundOffset = True
                                break
                        if foundOffset:
                            break
                    for jj,scanJ in enumerate(scanners[j]):
                        newScanJ = [d*scanJ[a], e*scanJ[b], f*scanJ[c]]
                        scanners[j][jj] = [newScanJ[0]+offset[0], newScanJ[1]+offset[1], newScanJ[2]+offset[2]]
                        allBeacons.append(scanners[j][jj])
                        allBeacons = [list(tupl) for tupl in {tuple(item) for item in allBeacons }]
                    deducedScanners.append(j)
                    unknownScanners.remove(j)
                    break

maxDist = 0
for scannerA in scannerLocs:
    for scannerB in scannerLocs:
        dist = abs(scannerB[0]-scannerA[0]) + abs(scannerB[1]-scannerA[1]) + abs(scannerB[2]-scannerA[2])
        if dist>maxDist:
            maxDist = dist
print(maxDist)