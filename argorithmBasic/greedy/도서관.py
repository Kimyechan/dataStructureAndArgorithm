# n, m = map(int, input().split(' '))
# distance = list(map(int, input().split(' ')))
#
# distance.sort()
#
# distanceMinus = list()
# distancePlus = list()
#
# for i in distance:
#     if i < 0:
#         distanceMinus.append(i)
#     else:
#         distancePlus.append(i)
#
# moveMinus = []
#
# for i in range(0, len(distanceMinus), m):
#     moveMinus.append(distanceMinus[i])
#
# distancePlus.sort(reverse=True)
#
# movePlus = []
#
# for i in range(0, len(distancePlus), m):
#     movePlus.append(distancePlus[i])
#
# result = 0
#
# for i in range(len(moveMinus)):
#     result += abs(moveMinus[i]) * 2
#
# for i in range(len(movePlus)):
#     result += movePlus[i] * 2
#
# if abs(moveMinus[0]) > movePlus[0]:
#     result -= abs(moveMinus[0])
# else:
#     result -= movePlus[0]
#
# print(result)

import heapq

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

largest = max(max(array), - min(array))

for i in array:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0
while positive:
    result += heapq.heappop(positive)
    for _ in range(m - 1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - largest)
