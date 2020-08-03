N = int(input())
T = [list(map(int, input().split(' '))) for i in range(N)]

dp = []

for i in range(1, N + 1):
    line = [0 for x in range(i)]
    dp.append(line)

dp[0][0] = T[0][0]

for i in range(1, N):
    for j in range(len(T[i])):
        if 0 < j < len(T[i]) - 1:
            if i != 1:
                dp[i][j] = T[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = T[i][j] + dp[i-1][j]
        elif j == 0:
            dp[i][j] = T[i][j] + dp[i-1][j]
        elif j == len(T[i]) - 1:
            dp[i][j] = T[i][j] + dp[i-1][j-1]

print(max(dp[N-1]))