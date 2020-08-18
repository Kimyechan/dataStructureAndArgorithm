N, M = map(int, input().split())
A = [[0 for _ in range(M+1)] for _ in range(N+1)]

# DP[i][j]는 (i, j)까지 왔을 때, 가장 큰 정사각형의 한 변 길이
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, list(input())))):
        A[i+1][idx+1] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

print(max(max(i) for i in DP) ** 2)
