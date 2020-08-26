N = int(input())

countNum = 0

NT = N

while NT >= 1:
    NT /= 10
    countNum += 1

compareNum = 1
for _ in range(countNum-1):
    compareNum *= 10
    compareNum += 1
if N == 0:
    print(1)
else:
    if N < compareNum:
        print(countNum - 1)
    else:
        print(countNum)