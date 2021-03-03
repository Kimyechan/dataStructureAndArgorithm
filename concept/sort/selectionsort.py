# def selectionSort(data):
#     for stand in range(len(data) - 1):
#         lowest = stand
#         for index in range(stand+1, len(data)-1):
#             if data[lowest] > data[index]:
#                 lowest = index
#         data[stand], data[lowest] = data[lowest], data[stand]
#
#     return data
#
# import random
#
# data = random.sample(range(100), 10)
# print(selectionSort(data))


def selectionSort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data) - 1):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]

    return data

import random

data_list = random.sample(range(100), 50)
print(selectionSort(data_list))