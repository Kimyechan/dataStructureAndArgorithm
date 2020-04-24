import heapq
import sys

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    data1 = heapq.heappop(heap)
    data2 = heapq.heappop(heap)
    sum = data1 + data2
    result = result + sum
    heapq.heappush(heap, sum)

print(result)
