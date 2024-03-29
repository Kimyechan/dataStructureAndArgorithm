# import heapq
#
#
# def dijkstra(graph, start):
#
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = []
#     heapq.heappush(queue, [distances[start], start])
#
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#
#         if distances[current_node] < current_distance:
#             continue
#
#         for adjacent, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             if distance < distances[adjacent]:
#                 distances[adjacent] = distance
#                 heapq.heappush(queue, [distance, adjacent])
#
#     return distances

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# print(dijkstra(mygraph, 'A'))


import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_dis, current_node = heapq.heappop(queue)

        if distances[current_node] < current_dis:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_dis + weight

            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])

    return distances


print(dijkstra(mygraph, 'A'))














