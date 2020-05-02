stringArray = input()

count0 = 0
count1 = 0

if stringArray[0] == '0':
    count1 = 1
else:
    count0 = 1

for i in range(len(stringArray)-1):
    if stringArray[i] != stringArray[i+1]:
        if stringArray[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))