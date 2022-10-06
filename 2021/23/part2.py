import numpy as np
import copy
import math

mat = np.array([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['#', '#', 'A', '#', 'D', '#', 'B', '#', 'D', '#', '#'],
                ['#', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#', '#'],
                ['#', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#', '#'],
                ['#', '#', 'B', '#', 'C', '#', 'A', '#', 'C', '#', '#']])

hallway = [(0, 0), (0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (0, 10)]
columnIndexLetter = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
columnIndexNum = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
scores = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def isPathFree(mat, x1, y1, x2, y2):
    length = 0
    while x1 > 0:
        x1 -= 1
        length += 1
        if mat[x1, y1] != '.':
            return [False, 0]
    while y1 < y2:
        y1 += 1
        length += 1
        if mat[x1][y1] != '.':
            return [False, 0]
    while y1 > y2:
        y1 -= 1
        length += 1
        if mat[x1][y1] != '.':
            return [False, 0]
    while x1 < x2:
        x1 += 1
        length += 1
        if mat[x1, y1] != '.':
            return [False, 0]
    if x1 != x2 or y1 != y2:
        return [False, 0]
    return [True, length]

mini = math.inf

def find(mat, score, depth):
    global mini
    if np.array_equal(mat, [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#'],
                            ['#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#'],
                            ['#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#'],
                            ['#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#']]):
        if score < mini:
            mini = score
            print(mini)
        return
    for j in [2, 4, 6, 8]:
        if np.count_nonzero(mat[1:, j] == columnIndexNum[j]) + np.count_nonzero(mat[1:, j] == '.') != 4:
            for i in range(1, 5):
                if mat[i, j] != '.':
                    column = columnIndexLetter[mat[i, j]]
                    if np.count_nonzero(mat[1:, column] == mat[i, j]) + np.count_nonzero(mat[1:, column] == '.') != 4:
                        for (ii, jj) in hallway:
                            if mat[ii, jj] == '.':
                                possible, length = isPathFree(mat, i, j, ii, jj)
                                if possible:
                                    newMat = np.copy(mat)
                                    newMat[ii][jj] = newMat[i][j]
                                    newMat[i][j] = '.'
                                    find(newMat, score + length * scores[mat[i, j]], depth+1)
                    else:
                        possible, length = isPathFree(mat,i, j, 4 - np.count_nonzero(mat[1:, column] == mat[i, j]), column)
                        if possible:
                            newMat = np.copy(mat)
                            ii = 4 - np.count_nonzero(mat[1:, column] == mat[i, j])
                            jj = column
                            newMat[ii][jj] = newMat[i][j]
                            newMat[i][j] = '.'
                            find(newMat, score + length * scores[mat[i, j]], depth+1)
                    break

    for (i, j) in hallway:
        if mat[i, j] != '.':
            column = columnIndexLetter[mat[i, j]]
            if np.count_nonzero(mat[1:, column] == mat[i, j]) + np.count_nonzero(mat[1:, column] == '.') != 4:
                pass
            else:
                possible, length = isPathFree(mat, i, j, 4 - np.count_nonzero(mat[1:, column] == mat[i, j]), column)
                if possible:
                    newMat = np.copy(mat)
                    ii = 4 - np.count_nonzero(mat[1:, column] == mat[i, j])
                    jj = column
                    newMat[ii][jj] = newMat[i][j]
                    newMat[i][j] = '.'
                    find(newMat, score + length * scores[mat[i, j]], depth+1)


find(mat, 0, 0)
