# 시간초과
N, A = int(input()), list(map(int, input().split()))
M, B = int(input()), list(map(int, input().split()))


A.sort()


def find(data1, data2):
    mid = int(len(data1) // 2)
    if data1[mid] == data2:
        return 1
    if data1[mid] != data2 and len(data1) == 1:
        return 0

    if data1[mid] < data2:
        return find(data1[mid:], data2)
    else:
        return find(data1[:mid], data2)


result = []


for data in B:
    a = find(A, data)
    if a:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)
