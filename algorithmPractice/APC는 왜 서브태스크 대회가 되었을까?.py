N, L, K = map(int, input().split())

easy = []
difficult = []
for _ in range(N):
    easyScore, difficultScore = map(int, input().split())
    easy.append(easyScore)
    difficult.append(difficultScore)

totalScore = 0
count = 0
select = []

for i in range(N):
    if easy[i] <= L and difficult[i] <= L:
        select.append(i)

if len(select) >= K:
    totalScore = 140 * K
else:
    totalScore = 140 * len(select)
    i = 0
    while len(select) + count != K and i <= N-1:
        if easy[i] <= L and difficult[i] > L:
            totalScore += 100
            count += 1
        i += 1

print(totalScore)
