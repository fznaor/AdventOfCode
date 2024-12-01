file1 = open('input.txt', 'r')
lines = file1.readlines()

currLine = 0
commands = []
vals = {
    'a':0,
    'b':0,
    'c':0,
    'd':0
}

for line in [line.strip() for line in lines]:
    segments = line.split()
    commands.append(segments)

while currLine < len(lines):
    command = commands[currLine]
    if command[0] == 'cpy':
        if command[1].isdigit():
            vals[command[2]] = int(command[1])
        else:
            vals[command[2]] = vals[command[1]]
    elif command[0] == 'inc':
        vals[command[1]] += 1
    elif command[0] == 'dec':
        vals[command[1]] -= 1
    elif command[0] == 'jnz':
        if command[1].isdigit():
            if int(command[1]) != 0:
                currLine += int(command[2])
                continue
        elif vals[command[1]] != 0:
            currLine += int(command[2])
            continue
    currLine += 1
print(vals['a'])