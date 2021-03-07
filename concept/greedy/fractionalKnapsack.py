data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def getMaxValue(dataList, capacity):
    dataList = sorted(dataList, key=lambda x: x[1] / x[0], reverse=True)
    detail = list()

    value = 0

    for data in dataList:
        if capacity - data[0] >= 0:
            value += data[1]
            capacity -= data[0]
            detail.append(data)
        else:
            value += data[1] * (capacity / data[0])
            detail.append(data)
            break

    return value, detail


print(getMaxValue(data_list, 30))