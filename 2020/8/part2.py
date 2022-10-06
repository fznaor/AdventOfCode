file1 = open('input.txt', 'r')
lines = file1.readlines()

instructions = []
acc = 0
gotToEnd = False

for line in lines:
    line = line.rstrip().split(' ')
    line[1] = int(line[1])
    line.append(False)
    instructions.append(line)
    
def doInstruction(i):
    global acc, gotToEnd
    if i >= len(instructions):
        gotToEnd = True
        return
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
        
for instruction in instructions:
    acc = 0
    prevValue = None
    if instruction[0] == 'nop':
        prevValue = 'nop'
        instruction[0] = 'jmp'
    elif instruction[0] == 'jmp':
        prevValue = 'jmp'
        instruction[0] = 'nop'
    else:
        continue
    doInstruction(0)
    if gotToEnd:
        break
    instruction[0] = prevValue
    for ii in instructions:
        ii[2] = False
    
print(acc)