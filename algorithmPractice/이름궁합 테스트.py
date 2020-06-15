N, M = map(int, input().split())
aName, bName = input().split()

alpabat = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

combination = []

if len(aName) <=  len(bName):
    for i in range(len(aName)):
        combination.append(aName[i])
        combination.append(bName[i])
    for i in range(len(aName), len(bName)):
        combination.append(bName[i])
else:
    for i in range(len(bName)):
        combination.append(aName[i])
        combination.append(bName[i])
    for i in range(len(bName), len(aName)):
        combination.append(aName[i])

wordNumber = []

for word in combination:
    wordNumber.append(alpabat[ord(word) % 65])

while True:
    wordNumberTemp = []
    if len(wordNumber) == 2:
        break
    for i in range(len(wordNumber)-1):
        wordNumberTemp.append((wordNumber[i] + wordNumber[i+1]) % 10)
    wordNumber = wordNumberTemp

if wordNumber[0] == 0:
    wordNumber.pop(0)

for num in wordNumber:
    print(num, end="")
print("%")




