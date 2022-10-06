file1 = open('input.txt', 'r')
lines = file1.readlines()

instructions = []
acc = 0

for line in lines:
    line = line.rstrip().split(' ')
    line[1] = int(line[1])
    line.append(False)
    instructions.append(line)
    
def doInstruction(i):
    global acc
    if instructions[i][2]:
        return
    instructions[i][2] = True
    if instructions[i][0] == 'nop':
        doInstruction(i+1)
    elif instructions[i][0] == 'acc':
        acc += instructions[i][1]
        doInstruction(i+1)
    else:
        doInstruction(i+instructions[i][1])
        
doInstruction(0)
print(acc)