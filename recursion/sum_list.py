import random
data = random.sample(range(100), 10)
print(data)

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

print(sum_list(data))