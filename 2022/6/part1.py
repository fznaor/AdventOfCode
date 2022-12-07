file1 = open('input.txt', 'r')
lines = file1.readlines()

arr = lines[0].strip()
for i in range(len(arr) - 4):
    if len(set([x for x in arr[i:i+4]])) == 4:
        print(i+4)
        break