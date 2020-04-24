# import heapq
#
# heap = []
# inputNumber = []
# result = []
# count = int(input())
#
# for _ in range(count):
#     inputNumber.append(int(input()))
#
# for num in inputNumber:
#     if num == 0:
#         if heap:
#             result.append(heapq.heappop(heap))
#         else:
#             result.append(0)
#     else:
#         heapq.heappush(heap, num)
#
# for i in result:
#     print(i)

import heapq

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)
