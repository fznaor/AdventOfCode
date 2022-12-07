inp = "hepxxyzz"

def incrementString(s,i):
    s[i] = chr(ord(s[i])+1)
    if s[i] > 'z':
        s[i] = 'a'
        if i > 0:
            incrementString(s,i-1)
            
def isValid(p): 
    if 'i' in p or 'o' in p or 'l' in p:
        return False
    
    found1 = False
    for i in range(len(p)-2):
        if ord(p[i])+2 == ord(p[i+1])+1 == ord(p[i+2]):
            found1 = True
            break
    if not found1:
        return False
    
    found2 = 0
    skipNext = False
    for i in range(len(p)-1):
        if skipNext:
            skipNext = False
            continue
        if p[i] == p[i+1]:
            found2 += 1
            skipNext = True
    return found2 >= 2
    

inp = [x for x in inp]
while True:
    incrementString(inp,len(inp)-1)
    s = ''.join(inp)
    if isValid(s):
        print(s)
        break
    
    