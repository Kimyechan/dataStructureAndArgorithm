N, K = map(int, input().split(' '))
M = [list(input()) for _ in range(N)]

count = 0
changeCK = True
ck = [[False for i in range(10)] for i in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count

    ck[x][y] = True
    count += 1
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= N or y + dy[i] < 0 or y + dy[i] >= 10:
            continue
        if M[x][y] != '0' and M[x][y] == M[x + dx[i]][y + dy[i]] and not ck[x + dx[i]][y + dy[i]]:
            dfs(x + dx[i], y + dy[i])


while changeCK:
    changeCK = False

    for i in range(N):
        for j in range(10):
            if M[i][j] != '0' and not ck[i][j]:
                dfs(i, j)
                if count >= K:
                    for a in range(N):
                        for b in range(10):
                            if ck[a][b]:
                                M[a][b] = '0'
                    changeCK = True

                count = 0
                ck = [[False for i in range(10)] for i in range(N)]

    T = [list('0' for _ in range(N)) for _ in range(10)]

    for w in range(10):
        for h in range(N):
            T[w][h] = M[h][w]

    for w in range(10):
        for h in range(N):
            if T[w][-1] == '0':
                T[w].pop(-1)
                T[w].insert(0, '0')

    for w in range(10):
        for h in range(N):
            M[h][w] = T[w][h]


for i in range(N):
    for j in range(10):
        print(M[i][j], end='')
    print()