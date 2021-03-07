# def bfs(graph, start_node):
#     visited = list()
#     need_visit = list()
#
#     need_visit.append(start_node)
#
#     while need_visit:
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#
#     return visited

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# print(bfs(graph, 'A'))


def bfs(graph, start):
    visited = list()
    visit_need = list()

    visit_need.append(start)

    while visit_need:
        v = visit_need.pop(0)
        if v not in visited:
            visited.append(v)
            visit_need.extend(graph[v])

    return visited


print(bfs(graph, 'A'))


from collections import deque


n = 8
visited = [False] * n
adj = [[] for _ in range(n)]


def bfs2(s):
    q = deque([s])
    visited[s] = True

    while q:
        v = q.popleft()
        print(v)
        for a in adj[v]:
            if not visited[a]:
                visited[a] = True
                q.append(a)