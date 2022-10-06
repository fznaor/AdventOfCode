import numpy as np
import copy

file1 = open('input.txt', 'r')
lines = file1.readlines()

algo = [c for c in lines[0].rstrip()]
img = []

for i in range(2,len(lines)):
    row = [c for c in lines[i].rstrip()]
    img.append(row)

img = np.array(img)


for itera in range(50):
    if itera % 2 == 1:
        img = np.pad(img, pad_width=1, mode='constant', constant_values='#')
    else:
        img = np.pad(img, pad_width=1, mode='constant', constant_values='.')
    imgn = copy.deepcopy(img)
    for i in range(0, imgn.shape[1]):
        for j in range(0, imgn.shape[1]):
            index = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    try:
                        if img[ii][jj] == '#':
                            index = (index << 1) | 1
                        else:
                            index = (index << 1) | 0
                    except IndexError:
                        if itera % 2 ==1:
                            index = (index << 1) | 1
                        else:
                            index = (index << 1) | 0
            imgn[i][j] = algo[index]
    img = copy.deepcopy(imgn)
print((img == '#').sum())