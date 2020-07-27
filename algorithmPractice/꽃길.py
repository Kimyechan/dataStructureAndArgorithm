# S = int(input())
# M = [list(map(int, input().split(' '))) for i in range(S)]
#
# ck = [list(True for _ in range(S)) for _ in range(S)]
# dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
#
# result = 0
#
# for _ in range(3):
#     minCost = 10001
#     minX, minY = 0, 0
#     for i in range(1, S - 1):
#         for j in range(1, S - 1):
#             finalCk = True
#             for index in range(5):
#                 if not ck[i + dx[index]][j + dy[index]]:
#                     finalCk = False
#                     break
#
#             if finalCk:
#                 cost = 0
#                 for index in range(5):
#                     cost += M[i + dx[index]][j + dy[index]]
#                 if minCost > cost:
#                     minCost = cost
#                     minX, minY = i, j
#
#     for index in range(5):
#         ck[minX + dx[index]][minY + dy[index]] = False
#
#     result += minCost
#
# print(result)
N = int(input())
G = [list(map(int, input().split(' '))) for i in range(N)]

dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
result = 99999


def cost(lst):
    value = 0
    spot = []
    for location in lst:
        x = location // N
        y = location % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 99999
        for index in range(5):
            spot.append((x+dx[index], y+dy[index]))
            value += G[x+dx[index]][y+dy[index]]

    if len(set(spot)) != 15:
        return 99999
    return value


for i in range(N*N):
    for j in range(i+1, N*N):
        for z in range(j+1, N*N):
            result = min(result, cost([i, j, z]))

print(result)