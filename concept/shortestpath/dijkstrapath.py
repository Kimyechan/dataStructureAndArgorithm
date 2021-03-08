import heapq

def dijkstra(graph, start, end):
    distances = {vertex: [float('inf'), start] for vertex in graph}
    distances[start] = [0, start]
    queue = []

    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_vertex = heapq. heappop(queue)

        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]

    path_output += start

    print(path_output)

    return distances


def dijkstra2(graph, start, end):
    distances = {vertex: [float('inf'), start] for vertex in graph}
    distances[start] = [0, start]
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_dis, current_node = heapq.heappop(queue)

        if distances[current_node][0] < current_dis:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_dis + weight

            if distance < distances[adj][0]:
                distances[adj] = [distance, current_node]
                heapq.heappush(queue, [distance, adj])

    path = end
    path_output = path + "->"
    while distances[path][1] != start:
        path_output += distances[path][1] + "->"
        path = distances[path][1]

    path_output += start
    print(path_output)

    return distances


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A', 'F'))
print(dijkstra2(mygraph, 'A', 'F'))
