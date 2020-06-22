max = []
current = []


for _ in range(3):
    N, M = map(int, input().split())
    max.append(N)
    current.append(M)


def mix():
    for i in range(3):
        if max[(i+1) % 3] >= current[i] + current[(i+1)%3]:
            current[(i+1) % 3] += current[i]
            current[i] = 0
        else:
            remain = max[(i+1) % 3] - current[(i+1) % 3]
            current[(i + 1) % 3] = max[(i+1) % 3]
            current[i] -= remain


for _ in range(33):
    mix()

if max[1] >= current[0] + current[1]:
    current[1] += current[0]
    current[0] = 0
else:
    remain = max[1] - current[1]
    current[1] = max[1]
    current[0] -= remain

for x in current:
    print(x)