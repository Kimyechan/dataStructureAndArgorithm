# def qsort(data):
#     if len(data) <= 1:
#         return data
#
#     left, right = list(), list()
#     pivot = data[0]
#
#     for index in range(1, len(data)):
#         if pivot > data[index]:
#             left.append(data[index])
#         else:
#             right.append(data[index])
#
#     return qsort(left) + [pivot] + qsort(right)
#
# import random
#
# data_list = random.sample(range(100), 10)
#
# print(qsort(data_list))


def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    for i in range(1, len(data)):
        if data[i] <= pivot:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right)


def qsort2(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if item <= pivot]
    right = [item for item in data[1:] if item > pivot]

    return qsort2(left) + [pivot] + qsort2(right)


import random

data_list = random.sample(range(100), 50)

print(qsort(data_list))
print(qsort2(data_list))

























