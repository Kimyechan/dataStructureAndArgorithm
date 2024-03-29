def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


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

print(dfs(graph, 'A'))


def dfs2(graph, startNode):
    visited, need_visit = list(), list()
    need_visit.append(startNode)

    while need_visit:
        v = need_visit.pop()
        if v not in visited:
            visited.append(v)
            need_visit.extend(graph[v])

    return visited


visited = []


def dfs3(v):
    print(v, end=' ')
    visited.append(v)

    for a in graph[v]:
        if a not in visited:
            dfs3(a)


print(dfs2(graph, 'A'))
dfs3('A')
