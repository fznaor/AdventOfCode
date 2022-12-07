inp = "1113222113"

for i in range(50):
    newInp = ""
    countInRow = 0
    for ind,sign in enumerate(inp):
        countInRow += 1
        if ind < len(inp) - 1:
            if inp[ind+1] == inp[ind]:
                continue
            else:
                newInp += str(countInRow) + str(inp[ind])
                countInRow = 0  
        else:
            newInp += str(countInRow) + str(inp[ind])
            countInRow = 0           
    inp = newInp
print(len(inp))