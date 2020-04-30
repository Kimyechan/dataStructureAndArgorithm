# from collections import deque
#
# n = int(input())
# m = int(input())
# visited = [False] * (n + 1)
# adj = [[] for _ in range(n+1)]
#
# for i in range(m):
#     x, y = map(int, input().split())
#     adj[x].append(y)
#     adj[y].append(x)
#
# count = 0
#
#
# def bfs(v):
#     global count
#     q = deque([v])
#
#     while q:
#         v = q.popleft()
#         if not visited[v]:
#             count += 1
#             visited[v] = True
#             for e in adj[v]:
#                 if not visited[e]:
#                     q.append(e)
#
#
# bfs(1)
# print(count-1)
n = int(input())
m = int(input())
visited = [False] * (n + 1)
adj = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

count = 0


def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)


dfs(1)
print(count - 1)
















