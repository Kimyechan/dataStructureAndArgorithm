# N = int(input())
# chu = list(map(int, input().split()))
#
# chu.sort(reverse=True)
# chuMax = 2000000
# chuOrder = list()
#
# for num in range(1, chuMax+1):
#     checkNum = num
#     for chuValue in chu:
#         if chuValue <= checkNum:
#             checkNum -= chuValue
#     if checkNum == 0:
#         chuOrder.append(num)
#
#     if len(chuOrder) >= 2:
#         if chuOrder[-1] - chuOrder[-2] != 1:
#             break
#
# print(chuOrder[-2] + 1)
N, A = int(input()), sorted(list(map(int, input().split())))

ans = 0

for i in A:
    if i <= ans + 1:
        ans += i
    else:
        break

print(ans + 1)