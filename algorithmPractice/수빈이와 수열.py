N, lst = int(input()), list(map(int, input().split()))

result = []
for i in range(N):
    if i != 0:
        sumSequence = lst[i] * (i+1)
        for j in range(i):
            sumSequence = sumSequence - result[j]
        result.append(sumSequence)
    else:
        result.append(lst[i])

for i in result:
    print(i, end=" ")