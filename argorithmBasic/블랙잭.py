def blackJack(number, list):

    min = 300000
    for index1 in range(len(list)):
        for index2 in range(index1+1, len(list)):
            for index3 in range(index2+1, len(list)):
                sum = list[index1] + list[index2] + list[index3]
                if number - sum <= min and sum <= number:
                    min = number - sum
                    bestSum = sum

    return bestSum

count, number = list(map(int, input().split()))
list = list(map(int, input().split()))

print(blackJack(number, list))



