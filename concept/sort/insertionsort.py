# def insertionSort(data):
#     for index in range(len(data)-1):
#         for index2 in range(index+1, 0, -1):
#             if data[index2] < data[index2-1]:
#                 data[index2], data[index2-1] = data[index2-1], data[index2]
#             else:
#                 break
#     return data
#
# import random
# data_list = random.sample(range(100), 10)
# print(insertionSort(data_list))


def insertionSort(data):
    for i1 in range(len(data) - 1):
        for i2 in range(i1 + 1, 0, -1):
            if data[i2] < data[i2 - 1]:
                data[i2], data[i2 - 1] = data[i2 - 1], data[i2]
            else:
                break
    return data

import random

data_list = random.sample(range(100), 50)
print(insertionSort(data_list))