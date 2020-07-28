#틀린 문제~~
from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for i in range(N)]


def rotate90(Board, N):
    NB = deepcopy(Board)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = Board[i][j]  # 90도 회전 외우기
    return NB


def convert(lst, N):
    new_lst = [i for i in lst if i]
    for i in range(1, len(new_lst)):
        if new_lst[i] == new_lst[i-1]:
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i]
    return new_lst + [0] * (N - len(new_lst))


def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)

    return ret


print(dfs(N, Board, 5))


