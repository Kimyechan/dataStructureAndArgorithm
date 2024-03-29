# from collections import defaultdict
# from heapq import *
#
# def prim(start_node, edges):
#     mst = list()
#     adjacent_edges = defaultdict(list)
#     for weight, n1, n2 in edges:
#         adjacent_edges[n1].append((weight, n1, n2))
#         adjacent_edges[n2].append((weight, n2, n1))
#
#     connected_nodes = set(start_node)
#     candidate_edge_list = adjacent_edges[start_node]
#     heapify(candidate_edge_list)
#
#     while candidate_edge_list:
#         weight, n1, n2 = heappop(candidate_edge_list)
#         if n2 not in connected_nodes:
#             connected_nodes.add(n2)
#             mst.append((weight, n1, n2))
#
#             for edge in adjacent_edges[n2]:
#                 if edge[2] not in connected_nodes:
#                     heappush(candidate_edge_list, edge)
#
#     return mst

from collections import defaultdict
from heapq import *


def prim(start, edges):
    mst = list()
    adjEdges = defaultdict(list)

    for weight, n1, n2 in edges:
        adjEdges[n1].append([weight, n1, n2])
        adjEdges[n2].append([weight, n2, n1])

    connectedNodes = set(start)
    candidate_edge_list = adjEdges[start]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)

        if n2 not in connectedNodes:
            connectedNodes.add(n2)
            mst.append([weight, n1, n2])
            for edges in adjEdges[n2]:
                if edges[2] not in connectedNodes:
                    heappush(candidate_edge_list, edges)

    return mst


myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

print(prim ('A', myedges))




















