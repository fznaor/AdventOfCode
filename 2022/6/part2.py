file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = lines[0].strip()
for i in range(len(arr) - 14):
    if len(set([x for x in arr[i:i+14]])) == 14:
        print(i+14)
        break