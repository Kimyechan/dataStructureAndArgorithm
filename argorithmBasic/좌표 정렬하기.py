# n = int(input())
#
# array = []
#
# for _ in range(n):
#     x, y = map(int, input().split(' '))
#     array.append((x, y))
#
# array = sorted(array)
#
# for i in array:
#     print(i[0], i[1])

n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))

array = sorted(array, key=lambda x: x[0])

start = 0
count = 0
array2 = []

for i in range(len(array) - 1):
    if array[i][0] == array[i + 1][0]:
        array2.append(array[i])
