R, C = map(int, input().split())
M = [list(input()) for i in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for dis in range(4):
                x, y = i+dx[dis], j+dy[dis]
                if x < 0 or x >= R or y < 0 or y >= C:
                    continue
                if M[x][y] == 'S':
                    ck = True

if ck:
    print('0')
else:
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'WS':
                M[i][j] = 'D'
    print('1')
    for row in M:
        print(''.join(row))