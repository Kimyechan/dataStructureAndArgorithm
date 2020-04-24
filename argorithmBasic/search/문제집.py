import heapq

n, m = map(int, input().split())
order = [[] for i in range(n + 1)]
degree = [0] * (n+1)

for _ in range(m):
    first, second = map(int, input().split())
    order[first].append(second)
    degree[second] += 1

heap = []
result = []

for num in range(1, n+1):
    if degree[num] == 0:
        heapq.heappush(heap, num)

while heap:
    data1 = heapq.heappop(heap)
    result.append(data1)
    for data2 in order[data1]:
        degree[data2] -= 1
        if degree[data2] == 0:
            heapq.heappush(heap, data2)

for data in result:
    print(data, end=' ')