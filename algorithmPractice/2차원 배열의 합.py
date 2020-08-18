#메모리 초과
# N, M = map(int, input().split(' '))
# array = [list(map(int, input().split(' '))) for i in range(N)]
# K = int(input())
# spot = [list(map(int, input().split(' '))) for i in range(K)]
#
# dpH = [list(list(0 for _ in range(M)) for _ in range(M)) for _ in range(N)]
#
# for k in range(N):
#     for i in range(M):
#         for j in range(i, M):
#             dpH[k][i][j] = dpH[k][i][j-1] + array[k][j]
#
# for i in range(K):
#     x1 = spot[i][0]
#     y1 = spot[i][1]
#     x2 = spot[i][2]
#     y2 = spot[i][3]
#     result = 0
#     for j in range(x1-1, x2):
#         result += dpH[j][y1-1][y2-1]
#     print(result)
N, M = map(int, input().split(' '))
A = [list(map(int, input().split(' '))) for _ in range(N)]

# DP[i][j] = (1, 1)부터 (i, j)까지 합
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split(' '))
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])







