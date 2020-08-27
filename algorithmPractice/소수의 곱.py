import heapq
import copy

K, N = map(int, input().split())
p_list = list(map(int, input().split()))

lst, ck = copy.deepcopy(p_list), set()

heapq.heapify(lst)
count = 0

while count < N:
    minNum = heapq.heappop(lst)
    if minNum in ck:
        continue
    count += 1
    ck.add(minNum)
    for i in p_list:
        if minNum * i < 2 ** 32:
            heapq.heappush(lst, minNum * i)


print(minNum)