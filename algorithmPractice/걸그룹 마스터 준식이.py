N, M = map(int, input().split())

group = {}
for _ in range(N):
    groupName = input()
    K = int(input())
    name = list()
    for _ in range(K):
        name.append(input())
    name.sort()
    group[groupName] = name


def quiz(num, problem):
    if num == 0:
        for member in group[problem]:
            print(member)
    else:
        for data1 in group:
            for data2 in group[data1]:
                if data2 == problem:
                    print(data1)
                else:
                    continue


for _ in range(M):
    problem = input()
    num = int(input())
    quiz(num, problem)