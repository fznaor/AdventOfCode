card = 1327981
door = 2822615
mod = 20201227

i = 1
flag = False
cardFlag = False
doorFlag = False
val = 1
while True:
    val *= 7
    val %= mod
    if val == card:
        cardLoop = i
        cardFlag = True
    if val == door:
        doorLoop = i
        doorFlag = True
    if cardFlag and doorFlag:
        break
    i += 1

val = 1
for i in range(doorLoop):
    val *= card
    val %= mod
print(val)