from copy import deepcopy

N, A = int(input()), list(map(int, input().split(' ')))

# DP[i] : i까지 왔을 때, 합의 최대
DP = deepcopy(A)
rev = [i for i in range(N)]

idx = 0

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + A[i])
            rev[i] = j

    if DP[idx] < DP[i]:
        idx = i

while rev[idx] != idx:
    print(A[idx], sep=" ")
    idx = rev[idx]

print(A[idx])