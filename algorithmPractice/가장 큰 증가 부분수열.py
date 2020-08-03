from copy import deepcopy

N, A = int(input()), list(map(int, input().split(' ')))

# DP[i] : i까지 왔을 때, 합의 최대
DP = deepcopy(A)

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + A[i])

print(max(DP))
