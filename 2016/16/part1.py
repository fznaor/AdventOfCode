input = '00101000101111010'
diskLength = 272

while len(input) < diskLength:
    input += '0'
    for x in input[-2::-1]:
        notX = '1' if x == '0' else '0'
        input += notX
input = input[:diskLength]

while True:
    checksum = ''
    for (x,y) in zip(input[0::2], input[1::2]):
        if x == y:
            checksum += '1'
        else:
            checksum += '0'
    if len(checksum) % 2 == 1:
        print(checksum)
        break
    input = checksum