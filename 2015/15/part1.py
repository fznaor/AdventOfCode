file1 = open('input.txt', 'r')
lines = file1.readlines()

ingredients = dict()
for line in [line.strip().split(' ') for line in lines]:
    ingredients[line[0]] = dict()
    ingredients[line[0]]['cap'] = int(line[2][:-1])
    ingredients[line[0]]['dur'] = int(line[4][:-1])
    ingredients[line[0]]['fla'] = int(line[6][:-1])
    ingredients[line[0]]['tex'] = int(line[8][:-1])
    ingredients[line[0]]['cal'] = int(line[10])
    
hiScore = 0
for i in range(101):
    for j in range(101):
        if i+j > 100:
            break
        for k in range(101):
            if i+j+k > 100:
                break
            for l in range(101):
                if i+j+k+l == 100:
                    score = 0
                    indices = [i,j,k,l]
                    [cap,dur,fla,tex] = [0]*4
                    for index,ing in zip(indices,ingredients):
                        cap += ingredients[ing]['cap'] * index
                        dur += ingredients[ing]['dur'] * index
                        fla += ingredients[ing]['fla'] * index
                        tex += ingredients[ing]['tex'] * index
                    if cap < 0 or dur < 0 or fla < 0 or tex < 0:
                        score = 0
                    else:
                        score = cap*dur*fla*tex
                    if score > hiScore:
                        hiScore = score
print(hiScore)