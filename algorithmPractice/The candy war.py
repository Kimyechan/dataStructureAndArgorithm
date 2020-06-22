# N = int(input())
#
# for _ in range(N):
#     cycle = 0
#     success = True
#     check = 0
#     M, candy = int(input()), list(map(int, input().split()))
#
#     for i in range(len(candy)):
#         if candy[i] % 2 != 0:
#             candy[i] += 1
#
#     while True:
#         if len(candy) == 1:
#             break
#
#         for i in range(len(candy)-1):
#             if candy[i] != candy[i+1]:
#                 success = False
#             else:
#                 check += 1
#
#         if check == len(candy) - 1:
#             break
#
#         check = 0
#
#         temp = candy[:]
#         for i in range(len(candy)):
#             candy[i] = (candy[i] + temp[i-1]) // 2
#
#         for i in range(len(candy)):
#             if candy[i] % 2 != 0:
#                 candy[i] += 1
#
#         cycle += 1
#
#     print(cycle)


def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx + 1) % N] = candy[idx]

    for idx in range(N):
        candy[idx] += tmp_lst[idx]

    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for i in range(int(input())):
    process()














