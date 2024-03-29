# parent = dict()
# rank = dict()
#
# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]
#
# def union(node_v, node_u):
#     root1 = find(node_v)
#     root2 = find(node_u)
#
#     if rank[root1] > rank[root2]:
#         parent[root2] = root1
#     else:
#         parent[root1] = root2
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1
#
# def make_set(node):
#     parent[node] = node
#     rank[node] = 0
#
# def kruskal(graph):
#     mst = list()
#
#     for node in graph['vertices']:
#         make_set(node)
#
#     edges = graph['edges']
#     edges.sort()
#
#     for edge in edges:
#         weight, node_v, node_u = edge
#         if find(node_v) != find(node_u):
#             union(node_v, node_u)
#             mst.append(edge)
#
#     return mst

parent = dict()
rank = dict()


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(v, u):
    parent1 = find(v)
    parent2 = find(u)

    if rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2
        if rank[parent1] == rank[parent2]:
            rank[parent2] += 1


def makeSet(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    for node in graph['vertices']:
        makeSet(node)

    graph['edges'].sort()

    for weight, nodeV, nodeU in graph['edges']:
        if find(nodeV) != find(nodeU):
            union(nodeV, nodeU)
            mst.append([weight, nodeV, nodeU])

    return mst


mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

print(kruskal(mygraph))




