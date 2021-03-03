# def bubbleSort(data):
#     for index1 in range(len(data) - 1):
#         swap = False
#         for index2 in range(len(data) - index1 - 1):
#                 if data[index2] > data[index2 + 1]:
#                     data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
#                     swap = True
#
#         if swap == False:
#             break
#
#     return data
#
# import random
#
# data_list = random.sample(range(100), 50)
# print (bubbleSort(data_list))


def bubbleSort(data):
    for i1 in range(len(data) - 1):
        swap = False
        for i2 in range(len(data) - 1 - i1):
            if data[i2] > data[i2 + 1]:
                data[i2], data[i2 + 1] = data[i2 + 1], data[i2]
                swap = True

        if not swap:
            break

    return data


import random

data_list = random.sample(range(100), 50)
print(bubbleSort(data_list))















