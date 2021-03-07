# def binary_search(data, search):
#     print(data)
#     if len(data) == 1 and search == data[0]:
#         return True
#     if len(data) == 1 and search == data[0]:
#         return True
#     if len(data) == 0:
#         return False
#
#     medium = len(data) // 2
#     if search == data[medium]:
#         return True
#     else:
#         if search > data[medium]:
#             return binary_search(data[medium+1:], search)
#         else:
#             return binary_search(data[:medium], search)
#
# import random
#
# data = random.sample(range(100), 10)
# print(data.sort())
# print(binary_search(data, 1))


def binarySearch(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False

    mid = len(data) // 2
    if search == data[mid]:
        return True
    elif search > data[mid]:
        return binarySearch(data[mid:], search)
    elif search < data[mid]:
        return binarySearch(data[:mid], search)

import random

dataList = random.sample(range(50), 10)
dataList.sort()
print(dataList)
print(binarySearch(dataList, 25))




































